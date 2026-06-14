import os
import asyncio
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

MODEL = "us.amazon.nova-pro-v1:0"

async def main():
    # Connect to the AWS Documentation MCP server
    server_params = StdioServerParameters(
        command="uvx",
        args=["awslabs.aws-documentation-mcp-server@latest"],
        env={"FASTMCP_LOG_LEVEL": "ERROR"}
    )

    async with stdio_client(server_params) as (read, write):
        async with MCPClient(read, write) as mcp_client:
            tools = await mcp_client.list_tools()

            agent = Agent(
                model=MODEL,
                tools=tools,
                system_prompt="""You are an AWS documentation expert! 📚
You have access to the official AWS documentation via MCP tools.
Help users understand AWS services, find docs, and answer technical questions.
Always cite which AWS service or doc you're referencing."""
            )

            print("📚 AWS Docs Chatbot — powered by MCP")
            print("Ask me anything about AWS! Type 'quit' to exit.\n")

            while True:
                user_input = input("You: ").strip()
                if user_input.lower() in ["quit", "exit", "q"]:
                    print("Goodbye! 👋")
                    break
                if not user_input:
                    continue
                response = agent(user_input)
                print(f"Agent: {response}\n")

asyncio.run(main())

print("\n✅ Challenge 5 complete!")