SESSION 24 - TEST PIPELINE FILES (for the QodeBench support-bot)
================================================================
Put ALL these files INSIDE your existing support-bot folder
(next to rag_bot.py and company_faq.txt), then activate your venv.

INSTALL (once):
  source venv/bin/activate
  pip install deepeval giskard langfuse
  # promptfoo runs via npx, no install needed

FILES & HOW TO RUN (write one, run one):
  1. test_quality.py        -> python test_quality.py         (20 quality checks, pure Python)
  2. bot_provider.py +
     promptfooconfig.yaml    -> npx promptfoo@latest eval
                               then: npx promptfoo@latest view  (the 20-case grid)
  3. test_hallucination.py  -> python test_hallucination.py    (DeepEval hallucination)
  4. giskard_scan.py        -> python giskard_scan.py          (vulnerability report - SLOW, run before class)
  5. REDTEAM_STEPS.txt      -> follow the 3 steps               (red team - run before class)
  6. rag_bot_traced.py      -> python rag_bot_traced.py         (LangFuse tracing)

TEACHING ORDER (see the teaching script):
  Quality (test_quality OR promptfoo) -> DeepEval -> Security (red team + giskard) -> LangFuse
