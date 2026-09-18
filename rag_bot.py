from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k":3})

template = """You are a helpful customer support assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say
"I'am sorry, I don't have that information."

Context: {context}
Question: {question}
Answer:"""

prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs,
     "question": RunnablePassthrough()}
    | prompt #question + chunk
    | llm #openai + gpt 4o mini
    | StrOutputParser() # parsed and polised by parser
)

def ask(question: str) -> str:
    return rag_chain.invoke(question)