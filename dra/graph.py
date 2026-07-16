from . import agents


def build_graph():
    return {
        'coordinator': agents.coordinator,
        'source_hunter': agents.source_hunter,
        'historical': agents.historical_researcher,
        'verifier': agents.verifier,
        'perspective': agents.perspective_comparison,
        'report': agents.report_generator,
    }


def run_research(question):
    state = {'question': question}
    for _, node in build_graph().items():
        state.update(node(state))
    return state
