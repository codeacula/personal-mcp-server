from mcp.types import ToolDefinition, ToolParameter
from mcp.server import serve_tool
from datetime import datetime
import random
import requests

async def handle_get_status(args):
    try:
        ip = requests.get("https://api.ipify.org").text
    except Exception:
        ip = "Unavailable"

    return {
        "ip": ip,
        "datetime": datetime.utcnow().isoformat() + "Z",
        "random": random.randint(1, 100)
    }

tool = ToolDefinition(
    name="get_status",
    description="Returns your public IP, UTC datetime, and a random number.",
    parameters={
        "no_args": ToolParameter(type="string", required=False, description="Unused")
    },
    run=handle_get_status
)

if __name__ == "__main__":
    serve_tool(tool)
