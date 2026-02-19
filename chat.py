from app.retriever import get_retriever
from app.memory import save_user_memory, save_company_memory

retriever = get_retriever()
print("Chatbot ready. Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Retrieve relevant documents
    docs = retriever._get_relevant_documents(question, run_manager=None)

    # Build answer
    answer = ""
    for doc in docs:
        answer += f"{doc.page_content}\n(Source: {doc.metadata['source']})\n"

    print("\nBot:")
    print(answer)

    # Save memory here, not in memory.py
    save_user_memory(f"User asked: {question}")

    for doc in docs:
        snippet = doc.page_content.strip().replace("\n", " ")[:150]
        save_company_memory(f"Doc insight: {snippet}...")
