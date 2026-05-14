from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

AgentModel = ChatOpenAI(model="gpt-5.4")

UserQuery = input("Enter A Prompt/Question")
Response = AgentModel.invoke(UserQuery)
print(Response)
