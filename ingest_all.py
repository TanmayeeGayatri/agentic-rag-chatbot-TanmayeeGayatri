from app.ingest import ingest

print("Ingesting langchain.txt...")
ingest("sample_docs/langchain.txt")

print("\nIngesting rag.txt...")
ingest("sample_docs/rag.txt")

print("\nIngesting memory.txt...")
ingest("sample_docs/memory.txt")

print("\nAll documents ingested successfully.")
