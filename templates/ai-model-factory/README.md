# AI Model Factory & Domain GGUF Engine
### Enterprise Fine-Tuning, Quantization & 1-Click Deployment

This template provides an end-to-end autonomous model factory combining QLoRA parameter-efficient training, FP16 merging, `llama.cpp` domain-calibrated quantization, and 1-click Ollama / OpenAI API serving.

---

## Capabilities & Architecture
1. **QLoRA Fine-Tuning**: Trains 3B–7B parameter models (e.g., Qwen 2.5, LLaMA 3.2) using 4-bit NF4 quantization on single Turing T4 GPUs.
2. **Domain-Calibrated GGUFs**: Compiles `Q4_K_M`, `Q5_K_M`, and `Q8_0` binaries using `imatrix` domain importance matrices.
3. **Formal Benchmarking**: Automated evaluation across ARC Challenge, HellaSwag, and MMLU.
4. **1-Click Local Execution**: Includes PowerShell and Bash scripts for instant offline deployment with Ollama or a drop-in local OpenAI-compatible REST API.

---

## Quick Start

### 1. Fine-Tune on Domain Dataset
```bash
python train_qlora.py --base-model "Qwen/Qwen2.5-3B-Instruct" --dataset "your-dataset-name" --epochs 1
```

### 2. Quantize into GGUF
```bash
python quantize_gguf.py --merged-fp16-dir "./merged_model" --output-dir "./gguf_output"
```

### 3. Serve via Drop-In OpenAI API
```bash
python serve_openai_api.py --model "model-Q4_K_M.gguf" --port 8000
```
Then point your LangChain, Next.js, or internal chatbot to `http://localhost:8000/v1`!
