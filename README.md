# Barebones MCP Server

A minimal, dockerized template for creating HTTP-based Model Context Protocol (MCP) servers. This template provides a starting point for building your own MCP tools and services.

## Features

- **HTTP Transport**: Ready-to-use HTTP MCP server setup
- **Docker Support**: Containerized deployment with Python 3.13
- **FastMCP Framework**: Built using the FastMCP library for easy MCP server development
- **Template Structure**: Clean, minimal codebase to build upon

## What's Included

This template includes a simple `get_cat_fact()` tool as an example - replace it with your own tools and functionality.

## Quick Start

1. **Build and run the Docker container**:
   ```bash
   docker build -t mcp-server .
   docker run -p 8000:8000 mcp-server
   ```

2. **Connect in VS Code**:
   - Click the "Start" button on the `.vscode/mcp.json` file that appears in VS Code
   - The MCP server will be automatically configured and connected

3. **Access your tools**:
   - Open the Chat panel in VS Code
   - Click the wrench icon (🔧) to see available MCP tools
   - Your `get_cat_fact()` tool should appear and be ready to use
   - Test with prompts like:
     - "Do you see a cat fact mcp tool?"
     - "Get me a cat fact"
   - **Note**: The AI agent should prompt you that it will use an MCP tool before executing it. If you don't see this prompt, the tool isn't being used.

## MCP Configuration

Add this to your `.vscode/mcp.json` file:

```json
{
  "servers": {
    "my-mcp-tools": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

## Available Tools (Example)

- `get_cat_fact()`: Example tool that returns a random cat fact - replace with your own tools

## Debugging with MCP Inspector

For debugging and testing your MCP server, you can use the MCP Inspector:

1. **Install and run MCP Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Configure the connection**:
   - Set transport type to: `httpstreamable`
   - Set URL to: `http://localhost:8000/mcp`

3. **Test your tools**:
   - The inspector will show all available tools and their schemas
   - You can test each tool directly from the web interface
   - View server capabilities and debug any issues

## Customizing the Template

1. **Replace the example tool** in `server.py` with your own MCP tools
2. **Update dependencies** in `requirements.txt` as needed  
3. **Modify the server name** in the FastMCP constructor
4. **Add your tool logic** using the `@mcp.tool()` decorator
