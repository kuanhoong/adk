# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import LlmAgent 
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams 
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams 
from mcp import StdioServerParameters

# Retrieve the API key from an environment variable or directly insert it.
# Using an environment variable is generally safer.
# Ensure this environment variable is set in the terminal where you run 'adk web'.
# Example: export GITHUB_PERSONAL_ACCESS_TOKEN="YOUR_ACTUAL_KEY"

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='maps_assistant_agent',
    instruction='Help the user with mapping, directions, and finding places using Google Maps tools.',
    tools=[
       MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
            url="https://api.githubcopilot.com/mcp/",
            headers={
            "Authorization": "Bearer " + os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"),
        },
    ),
    # Read only tools
    tool_filter=[
        "search_repositories",
        "search_issues",
        "list_issues",
        "get_issue",
        "list_pull_requests",
        "get_pull_request",
    ],
)
    ],
)
