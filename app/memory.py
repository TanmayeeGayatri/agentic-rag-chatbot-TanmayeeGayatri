

USER_MEMORY_FILE = "USER_MEMORY.md"

def save_user_memory(text):
    if not text.strip():
        return
    with open(USER_MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"- {text}\n")


COMPANY_MEMORY_FILE = "COMPANY_MEMORY.md"

def save_company_memory(text):
    if not text.strip():
        return
    with open(COMPANY_MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"- {text}\n")
