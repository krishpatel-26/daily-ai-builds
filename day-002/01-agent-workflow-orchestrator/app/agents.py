from dataclasses import dataclass

@dataclass
class AgentContext:
    request: str

class BaseAgent:
    name='base'
    def run(self, objective: str, context: AgentContext) -> str:
        raise NotImplementedError

class ResearchAgent(BaseAgent):
    name='research'
    def run(self, objective, context): return f'Research brief for: {objective}'

class DataAgent(BaseAgent):
    name='data'
    def run(self, objective, context): return f'Data plan for: {objective}'

class GTMAgent(BaseAgent):
    name='gtm'
    def run(self, objective, context): return f'GTM plan for: {objective}'

class APIAgent(BaseAgent):
    name='api'
    def run(self, objective, context): return f'API design for: {objective}'

AGENTS={a.name:a for a in [ResearchAgent(),DataAgent(),GTMAgent(),APIAgent()]}
