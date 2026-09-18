from fastapi import FastAPI
from pydantic import BaseModel
from rag_bot import ask
from dotenv import load_dotenv
load_dotenv()  # Reads the .env file and sets the environment variables
from rag_bot import ask  # Must be imported AFTER load_dotenv()

app = FastAPI()
class Question(BaseModel):
    question: str

@app.post("/chat")

def chat(payload: Question): 
    return {"answer": ask(payload.question)}

