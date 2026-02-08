# ./adk_agent_samples/mcp_agent/agent.py
import os

# ADK imports
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.apps.app import App
from google.adk.a2a.utils.agent_to_a2a import to_a2a

# === Configuration ===
MCP_URL = (
    "https://mcp.connectjunction.io"
    "/api/v1/mcp/ed769f90b06f447b91ffba8319501483/P5gYpV6hWazQyza2m74ifJ4uFLVMV2kC"
)


DEFAULT_TOOL_FILTER = None


# === Agent definition ===
root_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="AgentJunction",
    instruction=(
        "You are AgentJunction's MCP-enabled assistant. "
        "When useful, call the MCP tools exposed by the connected server. IMPORTANT always wrap filter in double quotes before passing to the tool. This quotes are seprate from the ones used to call the tool."
    ),
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=MCP_URL,
            
            ),
            # Optional: filter tools to a specific set (None == allow all)
            tool_filter=DEFAULT_TOOL_FILTER,
        )
    ],
)



app = App(root_agent=root_agent, name="AgentJunction_A2A")

app = to_a2a(
    root_agent  
)
