from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

AgentModel = ChatOpenAI(model="gpt-5.4")
