from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
load_dotenv()
from langchain_core.prompts import PromptTemplate



if __name__ == "__main__":
    print("hello langchain")
    string_template = """You are my personal assistant. Like iron man jarvis. Answer me this {question}"""

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.0) # 0 to 1.0
    prompt = PromptTemplate(input_variables=["question"], template=string_template)

    chain = prompt | llm
    print(chain.invoke(input={"question": "Hello jarvis, is earth is safe or should i go to fight any alien today"}))
    print(chain.invoke(input={"question": ""}))


