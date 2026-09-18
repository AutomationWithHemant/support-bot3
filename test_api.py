import requests
from dotenv import load_dotenv

load_dotenv()

questions = [
    "How do I reset my password?",
    "What are your support hours?",
    "Do you accept cryptocurrency?",
    "What is the capital of France?",
]

for q in questions:
    response = requests.post(
        "http://localhost:8000/chat",
        json={"question": q}
    )

    print("Q:", q)

    # Check if the server responded with a successful status code (200)
    if response.status_code == 200:
        try:
            answer = response.json().get(
                "answer",
                "No answer key found in JSON response"
            )
            print("A:", answer)
        except Exception:
            print(
                "❌ Server sent a 200 OK but it wasn't valid JSON. "
                f"Raw text: {response.text}"
            )
    else:
        print(f"❌ Server error (Status Code {response.status_code})")
        print(f"   Raw Server Response: {response.text}")

    print("-" * 40)