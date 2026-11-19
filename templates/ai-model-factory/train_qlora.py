"""
Autonomous QLoRA Training Engine
--------------------------------
Parameter-Efficient Fine-Tuning (PEFT) on Turing T4 GPUs or local compute.
Features automatic FP16 GradScaler stabilization, BitsAndBytes 4-bit NF4 quantization,
and ChatML tokenization formatting.
"""

import argparse
import os
import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq
)


def run_training(
    base_model_id: str,
    dataset_name: str,
    output_dir: str,
    dataset_split: str = "train",
    epochs: int = 1,
    lora_r: int = 16,
    lora_alpha: int = 32,
    max_seq_length: int = 1024,
    learning_rate: float = 2e-4
):
    print(f"[+] Loading base tokenizer & model: {base_model_id}")
    tokenizer = AutoTokenizer.from_pretrained(base_model_id, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 4-bit Quantization Config (NF4)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.float16
    )

    model = AutoModelForCausalLM.from_pretrained(
        base_model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True
    )
    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        r=lora_r,
        lora_alpha=lora_alpha,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Turing T4 AMP stability cast
    for name, param in model.named_parameters():
        if param.requires_grad:
            param.data = param.data.to(torch.float32)

    print(f"[+] Ingesting dataset: {dataset_name} ({dataset_split})")
    raw_dataset = load_dataset(dataset_name, split=dataset_split)

    def format_prompts(batch):
        formatted = []
        for msgs in batch["messages"]:
            text = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=False)
            formatted.append(text)
        tokens = tokenizer(formatted, max_length=max_seq_length, truncation=True, padding=False)
        tokens["labels"] = [list(x) for x in tokens["input_ids"]]
        return tokens

    tokenized_dataset = raw_dataset.map(format_prompts, batched=True, remove_columns=raw_dataset.column_names)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        learning_rate=learning_rate,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        logging_steps=10,
        save_strategy="no",
        fp16=False,
        bf16=False,
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=DataCollatorForSeq2Seq(tokenizer, pad_to_multiple_of=8, return_tensors="pt")
    )

    print("[+] Starting QLoRA Fine-Tuning...")
    trainer.train()

    print(f"[+] Saving LoRA adapter weights to: {output_dir}")
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print("[✓] Training completed successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Autonomous QLoRA Trainer")
    parser.add_argument("--base-model", default="Qwen/Qwen2.5-3B-Instruct")
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--output-dir", default="./lora_adapter")
    parser.add_argument("--epochs", type=int, default=1)
    args = parser.parse_args()

    run_training(args.base_model, args.dataset, args.output_dir, epochs=args.epochs)
