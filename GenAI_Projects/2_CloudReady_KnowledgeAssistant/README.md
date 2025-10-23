# ☁️ Cloud-Ready Knowledge Assistant

> A lightweight Retrieval-Augmented Generation (RAG) chatbot deployed on **Hugging Face Spaces**.

🎯 **Objective:**  
Cloud ready RAG chatbot fully-hosted through Gradio app using only free-tier resources.

---

## 🧠 Overview
- Upload a PDF → text is chunked & embedded (LangChain + MiniLM).
- Retrieve top-k relevant chunks via FAISS.
- Generate concise answers with `google/flan-t5-base`.
- Hosted 100 % on Hugging Face Spaces (CPU only).

---

## 🛠 Tech Stack
| Category | Tools |
|-----------|--------|
| UI | **Gradio** |
| LLM | **Flan-T5 (Hugging Face)** |
| Embeddings | **sentence-transformers/all-MiniLM-L6-v2** |
| Retrieval | **FAISS + LangChain** |
| Hosting | **Hugging Face Spaces (Free)** |

---

## 🚀 Run Locally
```bash
git clone https://github.com/<yourusername>/cloud-knowledge-assistant.git
cd cloud-knowledge-assistant
pip install -r requirements.txt
python app_gradio.py