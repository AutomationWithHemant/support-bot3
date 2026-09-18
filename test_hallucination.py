"""
test_hallucination.py  -  measure hallucination on OUR RAG bot.
Run:  python test_hallucination.py
Low score = grounded in the FAQ.  High score = making things up.
"""
from dotenv import load_dotenv
load_dotenv()

from deepeval.metrics import HallucinationMetric,AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from rag_bot import ask

# the FAQ is our source of truth
faq = open("company_faq.txt").read()

questions = [
    "What are your support hours?",
    "How do I get a refund?",
    "Do you accept cryptocurrency?",     # out of scope - watch this one
    "What is the capital of France?",    # out of scope - watch this one
]

for q in questions:
    answer = ask(q)
    case = LLMTestCase(input=q, actual_output=answer, context=[faq])
    metric = HallucinationMetric(threshold=0.8)
    metric2 = AnswerRelevancyMetric(threshold=0.5)
    metric.measure(case)
    print("Q:", q)
    print("A:", answer)
    print("Hallucination score:", round(metric.score, 2))
    print("Reason:", metric.reason)
    print("-" * 60)
    metric2.measure(case)
    print("Q:", q)
    print("A:", answer)
    print("AnswerRelevancy score:", round(metric2.score, 2))
    print("Relevancy Reason:", metric2.reason)
    print("-" * 60)

