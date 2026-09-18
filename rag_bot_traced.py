"""
rag_bot_traced.py  -  same bot, but every call is traced with LangFuse.
This shows how to add monitoring to the pipeline.
Run:  python rag_bot_traced.py   (needs LangFuse keys in .env)
"""
from dotenv import load_dotenv
load_dotenv()

from langfuse import observe, get_client
from rag_bot import ask as _ask

@observe()                       # trace every call
def ask(question: str) -> str:
    return _ask(question)

if __name__ == "__main__":
    questions = [
        "What are your support hours?",
        "How do I get a refund?",
        "Do you accept cryptocurrency?",
    ]
    for q in questions:
        print("Q:", q)
        print("A:", ask(q))
        print("-" * 40)
    get_client().flush()         # REQUIRED: push traces to LangFuse
    print("Traces sent to LangFuse. Open your dashboard.")
