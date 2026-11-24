from .models import Node, Line, Network


def demo_network() -> Network:
    return Network(
        nodes=(
            Node('NORTH', .16, .14, 18, 3, 55),
            Node('WEST', .11, .50, 20, 2, 0),
            Node('CENTER', .43, .43, 32, 3, 28),
            Node('HOSPITAL', .78, .21, 23, 5, 0),
            Node('EAST', .88, .51, 26, 2, 42),
            Node('INDUSTRY', .63, .82, 34, 1, 0),
            Node('SOUTH', .26, .86, 22, 2, 43),
            Node('WATER', .88, .85, 14, 5, 0),
        ),
        lines=(
            Line('L01', 'NORTH','WEST', .12, 46),
            Line('L02', 'NORTH','CENTER', .16, 58),
            Line('L03', 'WEST','CENTER', .10, 38),
            Line('L04', 'WEST','SOUTH', .17, 44),
            Line('L05', 'CENTER','HOSPITAL', .11, 44),
            Line('L06', 'CENTER','EAST', .10, 54),
            Line('L07', 'CENTER','INDUSTRY', .18, 40),
            Line('L08', 'HOSPITAL','EAST', .13, 35),
            Line('L09', 'EAST','WATER', .13, 34),
            Line('L10', 'INDUSTRY','WATER', .10, 33),
            Line('L11', 'INDUSTRY','SOUTH', .13, 42),
            Line('L12', 'SOUTH','CENTER', .22, 40),
        ),
    )


def validate(network: Network) -> None:
    ids = [x.id for x in network.nodes]
    if len(ids) != len(set(ids)) or not ids:
        raise ValueError('Network must have unique nonempty node IDs')
    lineids=set()
    for line in network.lines:
        if line.id in lineids or line.start not in ids or line.end not in ids or line.start == line.end:
            raise ValueError('Invalid line topology')
        if line.reactance <= 0 or line.limit <= 0:
            raise ValueError('Line reactance and limit must be positive')
        lineids.add(line.id)
    for n in network.nodes:
        if n.demand < 0 or n.generation_capacity < 0 or n.criticality not in (1,2,3,4,5):
            raise ValueError('Invalid node parameters')
