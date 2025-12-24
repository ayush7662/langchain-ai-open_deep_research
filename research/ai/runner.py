from .graph import research_graph

def run_research(query, previous_summary=None):
    input_data = {
        "query": query,
        "summary": previous_summary or "",
        "reasoning": "",
        "sources": []
    }

    # invoke graph WITHOUT callbacks
    result = research_graph.invoke(input_data)

    # tracing disabled for now
    trace_id = None

    return result, trace_id
