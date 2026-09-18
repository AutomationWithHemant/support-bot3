from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

docs = TextLoader("company_faq.txt").load()

chunks = RecursiveCharacterTextSplitter(
    chunk_size=300, chunk_overlap=50).split_documents(docs)

Chroma.from_documents(chunks,
                      OpenAIEmbeddings(model="text-embedding-3-small"),
                      persist_directory="./chroma_db")
