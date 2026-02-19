import json
import os

from app.ingest import ingest
from app.retriever import get_retriever


os.makedirs("artifacts", exist_ok=True)

# Step 1: ingest one document
ingest("sample_docs/rag.txt")

# Step 2: load retriever
retriever = get_retriever()

# Step 3: ask test question
question = "What is RAG?"

docs = retriever._get_relevant_documents(question, run_manager=None)

answer = ""
sources = []

for doc in docs:
    answer += doc.page_content + "\n"
    sources.append(doc.metadata["source"])

# Step 4: save output
output = {
    "question": question,
    "answer": answer.strip(),
    "sources": sources
}

with open("artifacts/sanity_output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)

print("sanity_output.json generated successfully.")
