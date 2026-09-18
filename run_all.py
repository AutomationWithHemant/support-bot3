from dotenv import load_dotenv
load_dotenv()
import datetime
from rag_bot import ask

cases = [
    ("What are your support hours?", ["monday"]),
    ("When can I reach support?", ["9", "monday"]),
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
    ("What is the capital of France?", ["don't have", "sorry"]),
    ("Do you accept cryptocurrency?", ["don't have", "sorry"]),
    ("Do you have an office in Mumbai?", ["don't have", "sorry"]),
    ("What's the weather today?", ["don't have", "sorry"]),
    ("Who is the CEO of QodeBench?", ["don't have", "sorry"]),
]

print("Running quality checks...")
results = []
passed = 0
for q, keywords in cases:
    answer = ask(q)
    ok = any(k.lower() in answer.lower() for k in keywords)
    results.append((q, answer, ok))
    if ok:
        passed += 1
    print(("  PASS " if ok else "  FAIL "), q)

score = f"{passed}/{len(cases)}"
print(f"\nQuality: {score} passed\n")

now = datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")
verdict = "READY" if passed >= len(cases) - 1 else "NEEDS WORK"
vcolor = "#22C55E" if verdict == "READY" else "#F59E0B"

rows = ""
for q, answer, ok in results:
    badge = "PASS" if ok else "FAIL"
    bcolor = "#22C55E" if ok else "#EF4444"
    rows += f'<tr><td>{q}</td><td style="color:#C4B5FD">{answer}</td><td><span style="background:{bcolor};color:#0A0A14;font-weight:bold;padding:3px 10px;border-radius:5px">{badge}</span></td></tr>'

html = f'''<!doctype html><html><head><meta charset="utf-8"><title>Test Report</title>
<style>body{{font-family:Arial;background:#0A0A14;color:#F1F1F6;padding:40px}}
table{{width:100%;border-collapse:collapse;background:#15151F;border-radius:10px;overflow:hidden}}
th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid #2A2A3E;font-size:14px}}
th{{background:#1B1B2E;color:#9CA3AF}}
.card{{background:#1A1A2E;border-radius:12px;padding:20px 26px;display:inline-block;margin:8px}}
</style></head><body>
<h1>QodeBench Support Bot - Test Report</h1>
<div style="color:#9CA3AF;margin-bottom:20px">Generated automatically by run_all.py &middot; {now}</div>
<div class="card"><div style="color:#9CA3AF;font-size:13px">Quality</div><div style="font-size:30px;font-weight:bold">{score}</div></div>
<div class="card"><div style="color:#9CA3AF;font-size:13px">Verdict</div><div style="font-size:30px;font-weight:bold;color:{vcolor}">{verdict}</div></div>
<table><tr><th>Question</th><th>Bot's answer</th><th>Result</th></tr>{rows}</table>
</body></html>'''

with open("quality_report.html", "w") as f:
    f.write(html)

print("=" * 50)
print("  DONE. Report created: quality_report.html")
print("=" * 50)