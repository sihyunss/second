!pip install -q openai
!pip install -q langchain
!pip install -q python-dotenv
!pip install -q pypdf
!pip install -U langchain-community
!pip install chromadb
!pip install tiktoken
!pip install -qU google-generativeai
!pip install -qU langchain-google-genai

import pandas as pd
import glob

import os

from langchain.document_loaders import PyPDFLoader

from langchain.embeddings.cohere import CohereEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain

from langchain_google_genai import ChatGoogleGenerativeAI


from langchain.document_loaders import WebBaseLoader

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

api_key = 'AIzaSyCWsn9CaJ5SHiXdbpVFUS2aLattLFckHoE'
os.environ["GOOGLE_API_KEY"] = api_key

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/MyDrive/

import os
os.listdir()

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader('How to get started with Drive.pdf')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

print(len(documents[0].page_content))
documents[0].page_content


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") # gemini의 임베딩 모델
# embeddings = OpenAIEmbeddings() # openai 의 임베딩모델

vector_store = Chroma.from_documents(texts, embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

system_template="""
Use the following pieces of context to answer the users question shortly.
Given the following summaries of a long document and a question, create a final answer with references ("SOURCES"), use "SOURCES" in capital letters regardless of the number of sources.
If you don't know the answer, just say that "I don't know", don't try to make up an answer.
----------------
{summaries}

You MUST answer in Korean and in Markdown format:"""

messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}")
]

prompt = ChatPromptTemplate.from_messages(messages)

chain_type_kwargs = {"prompt": prompt}

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             convert_system_message_to_human=True) # gemini pro 모델
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)  # openai의 gpt-3.5-turbo 모델


chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever = retriever,
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs)

query = "주제가 뭐야?"
result = chain(query)
result['answer']

query = "주제에 대해 더 자세히 설명해줘"
result = chain(query)
result['answer']

query = "구글 로그인하는 방법에 대해 알려줘"
result = chain(query)
result['answer']