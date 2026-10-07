from dataclasses import dataclass

@dataclass(frozen=True)
class Edge:
    source: str
    relation: str
    target: str

def neighbors(edges: list[Edge], node: str) -> list[str]:
    return [e.target for e in edges if e.source == node]
