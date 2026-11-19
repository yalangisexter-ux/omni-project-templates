#!/usr/bin/env bash
# Client 1-Click Deployment Script for macOS / Linux
# Usage: bash deploy_client_model.sh aryansexter/ronin-support-3b-GGUF Q4_K_M

REPO="${1:-aryansexter/ronin-support-3b-GGUF}"
QUANT="${2:-Q4_K_M}"
MODEL_NAME="${3:-client-custom-llm}"

echo "=========================================================="
echo " Deploying Private Model: $REPO [$QUANT]"
echo "=========================================================="

if ! command -v ollama &> /dev/null; then
    echo "Ollama is not installed. Please download it from https://ollama.com and run this script again."
    exit 1
fi

SLUG=$(echo "$REPO" | awk -F'/' '{print $NF}' | sed 's/-GGUF//')
FILE_NAME="${SLUG}-${QUANT}.gguf"
DOWNLOAD_URL="https://huggingface.co/${REPO}/resolve/main/${FILE_NAME}"

echo "Downloading calibrated GGUF from Hugging Face: ${DOWNLOAD_URL}..."
curl -L -o "${FILE_NAME}" "${DOWNLOAD_URL}"

echo "Building Ollama Modelfile..."
cat <<EOF > Modelfile
FROM ./${FILE_NAME}
PARAMETER temperature 0.3
PARAMETER top_p 0.9
EOF

echo "Registering model in Ollama..."
ollama create "${MODEL_NAME}" -f Modelfile

echo -e "\n Deployment Complete!"
echo "Run your private model anytime using:"
echo "    ollama run ${MODEL_NAME}"
echo -e "Or connect via local API at: http://localhost:11434/api/chat\n"
