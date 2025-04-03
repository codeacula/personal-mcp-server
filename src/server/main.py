import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def ping() -> str:
    """Ping the server."""
    return "pong"


if __name__ == "__main__":
    mcp.run()

