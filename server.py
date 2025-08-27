from fastmcp import FastMCP
import requests

# Create FastMCP server
mcp = FastMCP("Cat fact MCP")

@mcp.tool()
def get_cat_fact() -> str:
    """Gets a random cat fact from the cat facts API"""

    try:
        response = requests.get("https://catfact.ninja/fact")
        response.raise_for_status()
        data = response.json()
        return data.get("fact", "No cat fact available")
    except Exception as e:
        return f"Error fetching cat fact: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)