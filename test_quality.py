"""
test_quality.py  -  20 quality checks on OUR bot, pure Python (no extra tools).
Run:  python test_quality.py
Same idea as PromptFoo, but with zero setup - a safe fallback for class.
"""
from dotenv import load_dotenv
load_dotenv()
from rag_bot import ask

# (question, list of acceptable keywords - answer must contain at least one)
cases = [
    ("What are your support hours?", ["monday"]), #cases[0]
    ("When can I reach support?", ["9", "monday"]),#cases[1]
    ("How do I reset my password?", ["reset"]),
    ("I forgot my login details, what do I do?", ["reset", "password"]),
    ("What is your refund policy?", ["14 days", "refund"]),
    ("Can I get my money back?", ["refund"]),
    ("How do I upgrade my plan?", ["billing", "upgrade"]),
    ("Do you offer a free trial?", ["7", "trial"]),
    ("Is there a trial available?", ["trial"]),
    ("How can I contact a human agent?", ["support@qodebench.com", "email"]),
    ("Is my data secure?", ["encryption", "secure"]),
    ("What payment methods do you accept?", ["upi", "card"]),
    ("Can I pay with a credit card?", ["card"]),
    ("Can I cancel my subscription anytime?", ["cancel"]),
    ("How do I export my data?", ["export"]),
    # out-of-scope: bot should say it doesn't have the info
    ("What is the capital of France?", ["don't have", "sorry"]),
    ("Do you accept cryptocurrency?", ["don't have", "sorry"]),
    ("Do you have an office in Mumbai?", ["don't have", "sorry"]),
    ("What's the weather today?", ["don't have", "sorry"]),
    ("Who is the CEO of QodeBench?", ["don't have", "sorry"]),
]

passed = 0
for q, keywords in cases:
    answer = ask(q).lower() # VIP to vip
    ok = any(k.lower() in answer for k in keywords)
    print(("PASS " if ok else "FAIL "), q)
    if ok:
        passed += 1

print("-" * 60)
print(f"RESULT: {passed}/{len(cases)} passed")