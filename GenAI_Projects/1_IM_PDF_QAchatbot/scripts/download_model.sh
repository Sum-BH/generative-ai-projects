#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# Script: download_model.sh
# Purpose: Download a local LLM model (e.g., Mistral 7B GGUF) into ./models
# Usage:
#   bash scripts/download_model.sh
# -----------------------------------------------------------------------------

set -e  # stop if error occurs

# === CONFIGURATION SECTION ===
# 👉 Replace this with the Hugging Face model repository that contains your .gguf file.
# Example for Mistral GGUF: TheBloke/Mistral-7B-Instruct-v0.2-GGUF
MODEL_REPO="TheBloke/Mistral-7B-Instruct-v0.2-GGUF"

# 👉 Replace with the exact filename of the quantized model you want
MODEL_FILE="mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# Directory where model will be stored
DEST_DIR="./models"
mkdir -p "$DEST_DIR"

echo "📦 Downloading $MODEL_FILE from $MODEL_REPO ..."
echo "This may take several minutes depending on your internet speed."

# === DOWNLOAD MODEL USING huggingface_hub ===
python3 - <<PY
from huggingface_hub import hf_hub_download
import os

repo_id = "${MODEL_REPO}"
filename = "${MODEL_FILE}"
local_dir = os.path.abspath("${DEST_DIR}")

print(f"⬇️  Starting download: {repo_id}/{filename}")
path = hf_hub_download(repo_id=repo_id, filename=filename, local_dir=local_dir)
print(f"✅ Model downloaded to: {path}")
PY

echo "🎉 Done! Your model is now located in: ${DEST_DIR}/${MODEL_FILE}"
echo "Make sure your config.yaml points to this file under models.llm_path"