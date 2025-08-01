from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    })

    tools = await client.get_tools()

    model = ChatGroq(model="llama3-70b-8192")  
    agent = create_react_agent(model, tools)

    math_response = agent.invoke({
        "messages": [
            {"role": "user", "content": "what is (3+5)x2?"}
        ]
    })

    print(math_response['messages'][-1].content)

asyncio.run(main())
