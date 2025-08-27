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

### Local Development

1. **Set up Python environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the server**:
   ```bash
   python server.py
   ```

3. **Server will be available at**: `http://localhost:8000/mcp`

### Docker Deployment

1. **Build the image**:
   ```bash
   docker build -t mcp-server .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 mcp-server
   ```

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

## Customizing the Template

1. **Replace the example tool** in `server.py` with your own MCP tools
2. **Update dependencies** in `requirements.txt` as needed  
3. **Modify the server name** in the FastMCP constructor
4. **Add your tool logic** using the `@mcp.tool()` decorator
