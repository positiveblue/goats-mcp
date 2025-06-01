import os
import httpx
from fewsats.core import Fewsats
from mcp.server.fastmcp import FastMCP



# Create GOAT mcp
mcp = FastMCP("Fewsats MCP Server")

FEWSATS_API_KEY = os.getenv("FEWSATS_API_KEY")
print(FEWSATS_API_KEY)
fs = Fewsats(api_key=FEWSATS_API_KEY)


@mcp.tool()
def feed_goats() -> tuple[int, dict]:
    """
    Returns an L402 paywall for giving food to the goats.
    """
    offers_data = [{
        "id": "food-goats",
        "amount": 1,
        "currency": "USD",
        "description": "Feed the goats",
        "title": "Feed the goats",
        "payment_methods": ["lightning"]
    }]
    r = fs.create_offers(offers_data)
    offers = r.json()

    return 402, offers


if __name__ == "__main__":
    mcp.run()
