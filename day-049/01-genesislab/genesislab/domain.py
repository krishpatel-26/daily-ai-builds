"""Synthetic materials-process design domain. Not real chemistry or materials science."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Candidate:
    temperature: int
    speed: int

    @property
    def energy_index(self):
        return round(0.5 * self.temperature + 0.7 * self.speed, 2)

    def to_dict(self):
        return {'temperature': self.temperature, 'speed': self.speed,
                'energy_index': self.energy_index}


def safe(candidate):
    return (155 <= candidate.temperature <= 225
            and 20 <= candidate.speed <= 80
            and candidate.energy_index <= 158)


def candidates():
    return [c for t in range(155, 226, 5) for s in range(20, 81, 5)
            if safe(c := Candidate(t, s))]


def scaled(candidate):
    return ((candidate.temperature - 155) / 70, (candidate.speed - 20) / 60)
