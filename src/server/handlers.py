from src.server.command_handlers.ping_handler import handle_ping
from fastapi import HTTPException
from pydantic import BaseModel
import httpx
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

mcp = FastMCP()

@mcp.tool()
async def fetch_website(url: str) -> list[TextContent]:
    """Fetches a website and returns its content."""
    headers = {
        "User-Agent": "MCP Test Server (github.com/modelcontextprotocol/python-sdk)"
    }
    async with httpx.AsyncClient(follow_redirects=True, headers=headers) as client:
        response = await client.get(url)
        response.raise_for_status()
        return [TextContent(type="text", text=response.text)]

# Define Pydantic models for request bodies
class GreetRequest(BaseModel):
    name: str

class DataRequest(BaseModel):
    data: dict

# Update request handlers to use Pydantic models
def handle_request(request_type: str, request_body: dict = None):
    # Process the incoming request and return a response
    response = {}
    
    if request_type == 'greet':
        greet_request = GreetRequest(**request_body)
        response['message'] = f"Hello, {greet_request.name}!"
    elif request_type == 'ping':
        response = handle_ping()
    else:
        response['message'] = "Unknown request type."
    
    return response

def handle_data_request(data: DataRequest):
    # Process data-related requests
    response = {
        'status': 'success',
        'data': data.data
    }
    return response

def handle_error(error_message: str):
    # Handle errors and return an appropriate response
    raise HTTPException(status_code=400, detail=error_message)