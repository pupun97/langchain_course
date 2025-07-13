from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()


if __name__ == "__main__":
    print("hello langchain")
    string_template = """You are my personal assistant. Like iron man jarvis. Answer me this {question}"""

    llm = ChatOllama(model="llama3", temperature=1.0) # 0 to 10
    prompt = PromptTemplate(input_variables=["question"], template=string_template)

    chain = prompt | llm
    print(chain.invoke(input={"question": "Hello is earth is safe or should i go to fight any alien today"}))


