"""
giskard_scan.py  -  automatic vulnerability scan of OUR RAG bot (Giskard v3).
Run:  python giskard_scan.py
NOTE: makes many LLM calls and can take several minutes. Run BEFORE class.
Setup:  pip install --pre "giskard[scan,openai]" python-dotenv   (Python 3.12+)
"""
from dotenv import load_dotenv
load_dotenv()

import asyncio
import openai
from giskard.scan import vulnerability_scan
from rag_bot import ask


# 1. target: our bot, with retry + backoff so a 429 doesn't kill the scan
async def support_bot(inputs: str) -> str:
    for attempt in range(5):
        try:
            return str(await asyncio.to_thread(ask, inputs))
        except openai.RateLimitError:
            wait = 2 ** attempt * 5          # 5s, 10s, 20s, 40s, 80s
            print(f"  rate limited, retrying in {wait}s...")
            await asyncio.sleep(wait)
    return "ERROR: bot unavailable (rate limited)"


async def main() -> None:
    # 2. run the scan (it prints the grouped report itself)
    result = await vulnerability_scan(
        target=support_bot,
        description=(
            "A customer support assistant that answers questions about "
            "QodeBench using the company FAQ."
        ),
        languages=["en"],
        target_mode="singleturn",   # our bot has no chat memory -> skips multi-turn attacks
        max_scenarios=20,           # keep the demo small; raise later
        max_concurrency=2,          # only 2 attacks at a time -> stays under the rate limit
        return_exception=True,      # one failed attack is logged, the scan continues
    )

    # 3. save results (v3 has no HTML export)
    result.to_junit_xml("giskard_report.xml")
    with open("giskard_report.json", "w") as f:
        f.write(result.model_dump_json(indent=2))
    print(f"\nPass rate: {result.pass_rate}  |  "
          f"passed {result.passed_count}, failed {result.failed_count}, "
          f"errored {result.errored_count}")


asyncio.run(main())