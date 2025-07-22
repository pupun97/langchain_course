from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



if __name__ == "__main__":
    print("hello langchain")
    string_template = """You are my personal assistant. Like iron man jarvis. Answer me this {question}"""

    llm = ChatOllama(model="llama3", temperature=1.0) # 0 to 1.0
    prompt = PromptTemplate(input_variables=["question"], template=string_template)

    chain = prompt | llm | StrOutputParser()
    print(chain.invoke(input={"question": "Hello jarvis, is earth is safe or should i go to fight any alien today"}))
    print(chain.invoke(input={"question": ""}))


