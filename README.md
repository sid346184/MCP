🧠 LangGraph Multi-Server Reactive Agent
This project demonstrates how to build a React-style AI agent that uses LangChain, LangGraph, and Groq's LLaMA 3 model, connected to multiple tools (servers) via MultiServerMCPClient.

📌 Overview
Uses LangChain MCP (MultiServerMCPClient) to connect to different tools.

Implements a React Agent with LangGraph's create_react_agent.

Powered by Groq’s blazing fast LLaMA 3-70B for inference.

Integrates both:

A local math server via stdio transport

A weather server over HTTP

🏗️ Architecture
```
             +----------------------+
             |  Groq LLaMA 3 Model  |
             +----------------------+
                       |
         +-------------+----------------+
         |                              |
  +------+-----+                +-------+------+
  |  Math Tool  |               | Weather Tool |
  | (stdio)     |               | (HTTP MCP)   |
  +-------------+               +--------------+
```

Currently it is not connected to any weather api. Contributions are welcome ;)
