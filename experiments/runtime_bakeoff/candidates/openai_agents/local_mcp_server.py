"""Side-effect-free local MCP server for the OpenAI runtime candidate gate.

The server is deliberately tiny. It exists only to prove that the candidate can
consume a real stdio MCP tool through the released SDK integration rather than
through the pre-MCP in-process reference gateway used by the control harness.
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE


mcp = FastMCP("ads-methodological-reference")


@mcp.tool()
def lookup_methodological_reference(query: str) -> str:
    """Return one deterministic methodological reference for the supplied query."""

    return REFERENCE_FIXTURE.get(query, "no reference found")


if __name__ == "__main__":
    mcp.run(transport="stdio")
