from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_community.document_loaders import PyMuPDFLoader
import streamlit as st
load_dotenv()

st.title("Big Brother")

WebSearchTool = TavilySearch(max_result=5, topic="general")

#file_path = "./PDFData/PropInfo.pdf"
#loader = PyMuPDFLoader(file_path)
#docs = loader.load()
#print(len(docs))


AgentModel = ChatOpenAI(model="gpt-5.4", max_completion_tokens=1000, temperature=0.1)
Tools = [WebSearchTool]
SystemPrompt = "You are a General AI Information Assistant that Answers Questions and helps Users On general Everday Actives. When Questions are asks you find the *MOST UP TO DATE* sources from the current date regargding the subject and put these sources that use in a neatly fromatted list! When User Uploads documents Scan these doucments and do as the user asks with these documents"
Model = create_agent(AgentModel, tools=Tools, system_prompt=SystemPrompt)


while True:
    UserQuery = input("Enter A Prompt/Question: ")
    if UserQuery == "q" or UserQuery == "quit":
        break
        
    #Response = Model.invoke({"messages": [{"role": "user", "content": f"find Names in {docs}"}]})
    Response = Model.invoke({"messages": [{"role": "user", "content": UserQuery}]})
    print(Response["messages"][-1].content)
    

