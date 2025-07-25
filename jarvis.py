from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from tools.web import web_search
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


if __name__ == "__main__":
    print("hello langchain")
    string_template = """You are my personal assistant. Like iron man jarvis and you are also my financial advisor. Answer me this {question}"""

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.0) # 0 to 1.0
    prompt = PromptTemplate(input_variables=["question"], template=string_template)

    tools = [
        Tool(
            name="web_search",
            func= web_search,
            description="Use this tool to search the web for the latest news about a stock.",
        )
    ]

    agent_prompt = hub.pull("hwchase17/react")


    agent = create_react_agent(llm=llm, prompt=agent_prompt, tools=tools)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    resp = agent_executor.invoke({'input': prompt.invoke({"question": "What is date tommorow?"})})
    print(resp)


