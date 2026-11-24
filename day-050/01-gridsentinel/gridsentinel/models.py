from dataclasses import dataclass

@dataclass(frozen=True)
class Node:
    id: str
    x: float
    y: float
    demand: float
    criticality: int
    generation_capacity: float

@dataclass(frozen=True)
class Line:
    id: str
    start: str
    end: str
    reactance: float
    limit: float

@dataclass(frozen=True)
class Network:
    nodes: tuple[Node, ...]
    lines: tuple[Line, ...]
