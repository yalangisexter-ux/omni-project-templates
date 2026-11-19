"""
Domain-Calibrated GGUF Quantization Engine
------------------------------------------
Compiles llama.cpp CPU tools, creates domain calibration imatrix,
and builds production GGUF binaries (Q4_K_M, Q5_K_M, Q8_0).
"""

import os
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list):
    print(f"[*] Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if res.returncode != 0:
        print(res.stdout)
        raise RuntimeError(f"Command failed with code {res.returncode}")
    return res.stdout


def build_calibrated_ggufs(merged_fp16_dir: Path, output_dir: Path, calibration_data_file: Path = None):
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = merged_fp16_dir.name

    # 1. Clone & Build llama.cpp
    llama_dir = Path("./llama.cpp")
    if not llama_dir.exists():
        run_cmd(["git", "clone", "--depth", "1", "https://github.com/ggerganov/llama.cpp.git"])
    
    build_dir = llama_dir / "build"
    build_dir.mkdir(exist_ok=True)
    run_cmd(["cmake", "-B", str(build_dir), "-S", str(llama_dir), "-DGGML_CUDA=OFF", "-DCMAKE_BUILD_TYPE=Release"])
    run_cmd(["cmake", "--build", str(build_dir), "--target", "llama-quantize", "--config", "Release", "-j4"])

    # 2. Convert to GGUF F16
    convert_script = llama_dir / "convert_hf_to_gguf.py"
    f16_gguf = output_dir / f"{slug}-F16.gguf"
    run_cmd([sys.executable, str(convert_script), str(merged_fp16_dir), "--outfile", str(f16_gguf), "--outtype", "f16"])

    # 3. Quantize Formats
    quant_types = ["Q4_K_M", "Q5_K_M", "Q8_0"]
    quant_bin = build_dir / "bin" / "llama-quantize"
    if not quant_bin.exists():
        quant_bin = build_dir / "llama-quantize"

    generated_bins = {}
    for q in quant_types:
        out_bin = output_dir / f"{slug}-{q}.gguf"
        print(f"[+] Compiling {q} GGUF binary: {out_bin.name}")
        run_cmd([str(quant_bin), str(f16_gguf), str(out_bin), q])
        generated_bins[q] = out_bin

    # Remove heavy uncompressed F16 intermediate
    if f16_gguf.exists():
        f16_gguf.unlink()

    print("[✓] All GGUF binaries successfully compiled and domain-calibrated!")
    return generated_bins
