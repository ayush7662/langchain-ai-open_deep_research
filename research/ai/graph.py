from langgraph.graph import StateGraph
from typing import TypedDict, List

class ResearchState(TypedDict):
    query: str
    summary: str
    reasoning: str
    sources: List[str]

def planner(state):
    return {"reasoning": "Planned research steps"}

def researcher(state):
    return {
        "summary": f"Research result for: {state['query']}",
        "sources": ["example.com"]
    }

graph = StateGraph(ResearchState)
graph.add_node("plan", planner)
graph.add_node("research", researcher)
graph.set_entry_point("plan")
graph.add_edge("plan", "research")

research_graph = graph.compile()
