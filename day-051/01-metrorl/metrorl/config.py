from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    junctions: int = 3
    ticks: int = 160
    capacity: int = 36
    service: int = 3
    switch_lost_time: int = 1
    transfer_fraction: float = 0.30
    base_arrival: float = 1.05
    emergency_ticks: tuple = (32, 69, 115)

    def validate(self):
        if not 1 <= self.junctions <= 12 or not 1 <= self.ticks <= 2500:
            raise ValueError('Junctions/ticks outside supported simulation range')
        if not 1 <= self.service <= self.capacity or not 0 <= self.transfer_fraction <= 1:
            raise ValueError('Invalid service/capacity/transfer')
        if self.switch_lost_time not in (0, 1):
            raise ValueError('switch_lost_time must be 0 or 1')
        return self
