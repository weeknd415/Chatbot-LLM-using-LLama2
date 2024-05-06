from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os


os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="ls__82540b8d8f864814b38069e7a4b4cdac"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an AI assistant, help users with thier queries with informative knowledge."),
        ("user","Question:{question}")
    ]
)


st.title('Blog generation using langchain')
input_text=st.text_input("Search the topic u want")

# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
