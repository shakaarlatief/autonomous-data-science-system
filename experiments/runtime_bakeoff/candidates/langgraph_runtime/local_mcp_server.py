"""Side-effect-free stdio MCP reference server for the LangGraph candidate gate."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE


mcp = FastMCP("ads-langgraph-methodological-reference")


@mcp.tool()
def lookup_methodological_reference(query: str) -> str:
    """Return one deterministic methodological reference for the supplied query."""

    return REFERENCE_FIXTURE.get(query, "no reference found")


if __name__ == "__main__":
    mcp.run(transport="stdio")
