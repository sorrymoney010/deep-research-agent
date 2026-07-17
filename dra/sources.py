from __future__ import annotations

import requests
from .models import Citation, SourceTier

TIMEOUT = 15


def _get(url, params=None):
    try:
        r = requests.get(url, params=params, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None


def arxiv_search(query, limit=5):
    data = _get('https://export.arxiv.org/api/query', {'search_query': f'all:{query}', 'max_results': limit})
    return [] if not data else []


def crossref_search(query, limit=5):
    data = _get('https://api.crossref.org/works', {'query': query, 'rows': limit})
    results = []
    for item in (data or {}).get('message', {}).get('items', []):
        results.append(Citation(
            title=(item.get('title') or [''])[0],
            url=item.get('URL',''),
            tier=SourceTier.PRIMARY,
            author='Crossref'
        ))
    return results


def semantic_scholar_search(query, limit=5):
    data = _get('https://api.semanticscholar.org/graph/v1/paper/search', {'query':query,'limit':limit,'fields':'title,url,abstract'})
    results=[]
    for p in (data or {}).get('data',[]):
        results.append(Citation(title=p.get('title',''),url=p.get('url',''),snippet=p.get('abstract','') or '',tier=SourceTier.PRIMARY,author='Semantic Scholar'))
    return results


def inspire_search(query, limit=5):
    data = _get('https://inspirehep.net/api/literature', {'q':query,'size':limit})
    results=[]
    for item in (data or {}).get('hits',{}).get('hits',[]):
        meta=item.get('metadata',{})
        results.append(Citation(title=(meta.get('titles') or [{}])[0].get('title',''),url='https://inspirehep.net',tier=SourceTier.PRIMARY,author='INSPIRE-HEP'))
    return results


def gather(query, clients, limit=5):
    found=[]
    errors=[]
    for client in clients:
        try:
            if client=='crossref': found += crossref_search(query,limit)
            elif client=='semantic_scholar': found += semantic_scholar_search(query,limit)
            elif client=='inspire': found += inspire_search(query,limit)
        except Exception as e:
            errors.append(f'{client}: {e}')
    return found, errors

HISTORICAL_CLIENTS=['crossref']
