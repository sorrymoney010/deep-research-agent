import os

class LLMNotConfigured(Exception):
    pass

class LLMClient:
    def __init__(self):
        self.provider = None
        self.ready = False
        if os.getenv('GROQ_API_KEY'):
            self.provider = 'groq'
            self.ready = True
        elif os.getenv('OPENROUTER_API_KEY'):
            self.provider = 'openrouter'
            self.ready = True
        elif os.getenv('GEMINI_API_KEY'):
            self.provider = 'gemini'
            self.ready = True

    def complete(self, prompt: str):
        if not self.ready:
            raise LLMNotConfigured('No LLM API key configured')
        return ''

_client = None

def get_llm():
    global _client
    if _client is None:
        _client = LLMClient()
    return _client
