"""
☁️ Cloud-Ready Knowledge Assistant
- Robust file handling: only deletes temp files that this script created
- Works across repeated queries without needing re-upload
- Uses LangChain community imports and a CPU-friendly generator
"""

import os
import tempfile
import gradio as gr
from transformers import pipeline
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# -----------------------
# Model & Embeddings init
# -----------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
generator = pipeline("text2text-generation", model="google/flan-t5-base")

# -----------------------
# Helper: save uploaded PDF robustly and indicate ownership
# -----------------------
def _save_uploaded_pdf_to_temp(pdf_input):
    """
    Handle several Gradio input shapes and indicate whether we created the temp file.
    Returns: (pdf_path: str, created_temp: bool)
    created_temp == True => caller may safely delete the file after use.
    """
    # 1) If object has .name attribute and file exists -> Gradio/OS owns it
    try:
        if hasattr(pdf_input, "name") and isinstance(pdf_input.name, str) and os.path.exists(pdf_input.name):
            return pdf_input.name, False
    except Exception:
        pass

    # 2) If it's a string path that exists
    if isinstance(pdf_input, str) and os.path.exists(pdf_input):
        return pdf_input, False

    # 3) If it's a dict with "name" key and file exists
    if isinstance(pdf_input, dict) and "name" in pdf_input and os.path.exists(pdf_input["name"]):
        return pdf_input["name"], False

    # 4) Otherwise, create a temp file and write bytes/file-like contents — we own this file
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    try:
        if hasattr(pdf_input, "read"):
            data = pdf_input.read()
            if isinstance(data, str):
                data = data.encode("utf-8")
            tmp.write(data)
        elif isinstance(pdf_input, (bytes, bytearray)):
            tmp.write(pdf_input)
        else:
            tmp.write(str(pdf_input).encode("utf-8"))
    finally:
        tmp.flush()
        tmp.close()
    return tmp.name, True

# -----------------------
# Core function: PDF -> RAG -> answer
# -----------------------
def answer_question(question, pdf):
    if not question or not pdf:
        return "Please upload a PDF and enter a question."

    # Save uploaded PDF; know if we created the temp file
    pdf_path, created_temp = _save_uploaded_pdf_to_temp(pdf)

    # Basic existence check
    if not os.path.exists(pdf_path):
        return f"⚠️ Error: saved PDF path does not exist: {pdf_path}"

    # Quick header check to catch non-PDF inputs early
    try:
        with open(pdf_path, "rb") as fh:
            header = fh.read(8)
            if not header.startswith(b"%PDF"):
                return "⚠️ The uploaded file does not appear to be a valid PDF. Please upload a proper PDF file."
    except Exception:
        # If header read fails, let loader generate a clearer error
        pass

    try:
        # Load PDF and split into chunks
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        if not docs:
            return "⚠️ The PDF contained no readable text. Try a different PDF."

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = splitter.split_documents(docs)

        # Build FAISS vector store and retriever
        db = FAISS.from_documents(chunks, embeddings)
        retriever = db.as_retriever(search_kwargs={"k": 3})
        context_docs = retriever.get_relevant_documents(question)
        context = " ".join([d.page_content for d in context_docs])

        # Compose prompt and generate answer
        prompt = f"Answer the question using the context below.\n\nContext:\n{context}\n\nQuestion: {question}"
        answer = generator(prompt, max_length=256, clean_up_tokenization_spaces=True)[0].get("generated_text", "")

        return answer.strip() if answer else "⚠️ Model returned empty response."

    except Exception as e:
        # Return friendly error for UI debugging
        return f"⚠️ Error while processing PDF or generating answer: {e}"

    finally:
        # Delete temp file only if we created it in this function
        try:
            if created_temp and os.path.exists(pdf_path):
                os.remove(pdf_path)
        except Exception:
            pass

# -----------------------
# Gradio UI
# -----------------------
iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(label="💬 Ask a Question", placeholder="e.g., What are the key takeaways?"),
        gr.File(label="📄 Upload PDF (recommended < 5MB)")
    ],
    outputs=gr.Textbox(label="🧠 Answer"),
    title="☁️ Cloud-Ready Knowledge Assistant",
    description="Upload a PDF and ask contextual questions. Lightweight RAG using LangChain & Flan-T5 (CPU-friendly).",
    flagging_mode="never",
)

if __name__ == "__main__":
    iface.launch(share=False)