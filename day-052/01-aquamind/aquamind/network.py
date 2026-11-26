"""Small synthetic municipal distribution network, not an EPANET hydraulic model."""
from dataclasses import dataclass

RESERVOIR = 'SOURCE'
SOURCE_PRESSURE = 65.0

@dataclass(frozen=True)
class Junction:
    id: str
    x: float
    y: float
    demand: float

@dataclass(frozen=True)
class Pipe:
    id: str
    a: str
    b: str
    conductance: float

JUNCTIONS = (
    Junction('J-01', .15, .18, 2.0), Junction('J-02', .35, .10, 2.3),
    Junction('J-03', .61, .12, 2.7), Junction('J-04', .84, .24, 1.6),
    Junction('J-05', .19, .48, 2.1), Junction('J-06', .44, .44, 2.0),
    Junction('J-07', .72, .49, 2.4), Junction('J-08', .31, .78, 1.7),
    Junction('J-09', .66, .81, 1.8)
)
PIPES = (
    Pipe('P-01','SOURCE','J-01',4.0),Pipe('P-02','SOURCE','J-05',3.2),
    Pipe('P-03','J-01','J-02',2.5),Pipe('P-04','J-02','J-03',2.0),
    Pipe('P-05','J-03','J-04',1.9),Pipe('P-06','J-01','J-05',2.4),
    Pipe('P-07','J-02','J-06',2.5),Pipe('P-08','J-03','J-07',2.0),
    Pipe('P-09','J-04','J-07',1.7),Pipe('P-10','J-05','J-06',2.7),
    Pipe('P-11','J-06','J-07',2.6),Pipe('P-12','J-05','J-08',2.1),
    Pipe('P-13','J-06','J-08',1.6),Pipe('P-14','J-06','J-09',1.6),
    Pipe('P-15','J-07','J-09',2.0),Pipe('P-16','J-08','J-09',1.9)
)
SENSORS = ('J-01','J-02','J-03','J-05','J-06','J-07','J-08','J-09')

def graph_payload():
    return {'source': {'id':RESERVOIR,'x':.02,'y':.39,'pressure':SOURCE_PRESSURE},
            'junctions':[vars(j) for j in JUNCTIONS],
            'pipes':[vars(p) for p in PIPES], 'sensors':list(SENSORS),
            'units':'Synthetic pressure and demand units; not calibrated physical measurements'}
