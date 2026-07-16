def coordinator(state):
    return {'subquestions':[state['question']]}


def source_hunter(state):
    return {'citations':[], 'claims':[]}


def historical_researcher(state):
    return {'historical_sources':[]}


def verifier(state):
    return {'verified':True}


def perspective_comparison(state):
    return {'perspectives':[]}


def report_generator(state):
    return {'report':'Research pipeline complete'}
