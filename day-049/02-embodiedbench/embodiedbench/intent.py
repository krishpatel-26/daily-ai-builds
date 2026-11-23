"""Strict command grammar; no LLM and no free-form instruction execution."""
import re
from dataclasses import dataclass
from .world import ITEMS, ZONES

@dataclass(frozen=True)
class Task:
    item:str
    zone:str
    def id(self):return f'{self.item}->{self.zone}'

PATTERN = re.compile(r'\s*(?:move|deliver|place)\s+([a-z][a-z0-9_]*)\s+to\s+([a-z][a-z0-9_]*)\s*$',re.I)

def parse_instruction(text):
    match = PATTERN.fullmatch(text)
    if not match:
        raise ValueError('Expected: move ITEM to ZONE')
    item,zone=(x.lower() for x in match.groups())
    if item not in ITEMS or zone not in ZONES:
        raise ValueError('Item or destination is absent from the authoritative world')
    return Task(item,zone)


def sample_tasks():
    return [parse_instruction(text) for text in (
        'move red_cube to zone_a',
        'move blue_cylinder to zone_b',
        'move green_box to zone_c')]
