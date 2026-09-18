"""
dashboard.py  -  builds a quality dashboard from your pipeline results.
Run:  python dashboard.py   ->  prints a summary AND creates dashboard.html
Edit the numbers below to match YOUR bot's real results.
"""

# ---- YOUR real results from Session 24 (edit these) ----
metrics = [
    # (name,                    value,        status)   status: PASS / WATCH / FAIL
    ("Quality (PromptFoo)",     "19/20",      "PASS"),
    ("Hallucination (DeepEval)","0.0",        "PASS"),
    ("Security (Giskard)",      "0 issues",   "PASS"),
    ("Retrieval finding",       "1 (reworded)","WATCH"),
    ("Latency (LangFuse)",      "~3s",        "PASS"),
    ("Cost per query",          "<$0.01",     "PASS"),
]

# ---- print a clean text dashboard ----
print("\n" + "=" * 44)
print("   QODEBENCH SUPPORT BOT - QUALITY DASHBOARD")
print("=" * 44)
icon = {"PASS": "[PASS]", "WATCH": "[WATCH]", "FAIL": "[FAIL]"}
for name, value, status in metrics:
    print(f"  {name:<26} {value:<12} {icon[status]}")
print("=" * 44)

fails = [m for m in metrics if m[2] == "FAIL"]
watch = [m for m in metrics if m[2] == "WATCH"]
if fails:
    print("  VERDICT: NOT READY - fix failures first.")
elif watch:
    print("  VERDICT: READY with notes - review the WATCH items.")
else:
    print("  VERDICT: READY - all checks passed.")
print("=" * 44 + "\n")

# ---- also write an HTML version (nice for the presentation) ----
color = {"PASS": "#22C55E", "WATCH": "#F59E0B", "FAIL": "#EF4444"}
rows = ""
for name, value, status in metrics:
    rows += f'''
    <div class="card" style="border-color:{color[status]}">
      <div class="name">{name}</div>
      <div class="value">{value}</div>
      <div class="badge" style="background:{color[status]}">{status}</div>
    </div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8">
<title>Quality Dashboard</title>
<style>
  body {{ font-family: Arial, sans-serif; background:#0A0A14; color:#F1F1F6; padding:40px; }}
  h1 {{ text-align:center; }}
  .grid {{ display:flex; flex-wrap:wrap; gap:20px; justify-content:center; }}
  .card {{ background:#1A1A2E; border:2px solid; border-radius:12px; padding:20px; width:220px; }}
  .name {{ color:#9CA3AF; font-size:14px; }}
  .value {{ font-size:34px; font-weight:bold; margin:8px 0; }}
  .badge {{ display:inline-block; color:#0A0A14; font-weight:bold;
            padding:4px 12px; border-radius:6px; font-size:13px; }}
</style></head><body>
<h1>QodeBench Support Bot - Quality Dashboard</h1>
<div class="grid">{rows}</div>
</body></html>'''

with open("dashboard.html", "w") as f:
    f.write(html)
print("Also created dashboard.html - open it in a browser for the presentation.\n")
