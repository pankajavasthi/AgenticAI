from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from google.cloud import aiplatform



# Initialize the Vertex AI-backed Anthropic model
llm = ChatVertexAI(
    model="claude-3-5-sonnet@20240620",   # example Vertex model name for Anthropic
    project="lendo-dr-417012",
    location="us-central1",               # pick your region
    temperature=0.2,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful data engineering tutor."),
    ("user",   "Explain BigQuery partitions and clustering with a tiny SQL example.")
])

chain = prompt | llm | StrOutputParser()

print(chain.invoke({}))
