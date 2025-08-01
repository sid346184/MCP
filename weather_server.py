from mcp.server.fastmcp import  FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location)->str:
    """
    Get the weather location.
    """
    return "RAINY in California"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
# It will run like a server which can be used to get real time info
