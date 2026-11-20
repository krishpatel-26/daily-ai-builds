import heapq

WIDTH, HEIGHT = 16, 12
SHELVES = {(x, y) for x in (4, 5, 10, 11) for y in range(2, 10) if y not in (5, 6)}
CHARGERS = [(0, 0), (15, 11)]

def valid(p):
    x, y = p
    return 0 <= x < WIDTH and 0 <= y < HEIGHT and p not in SHELVES

def neighbors(p):
    x, y = p
    return [q for q in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)) if valid(q)]

def astar(start, goal):
    if not valid(start) or not valid(goal):
        return []
    dist = lambda p: abs(goal[0]-p[0]) + abs(goal[1]-p[1])
    heap = [(dist(start), 0, start)]
    best = {start:0}
    previous = {}
    while heap:
        _, steps, p = heapq.heappop(heap)
        if steps != best.get(p):
            continue
        if p == goal:
            route = [p]
            while p in previous:
                p = previous[p]
                route.append(p)
            return route[::-1]
        for next_cell in neighbors(p):
            new_cost = steps+1
            if new_cost < best.get(next_cell, 10**9):
                best[next_cell]=new_cost
                previous[next_cell]=p
                heapq.heappush(heap, (new_cost+dist(next_cell),new_cost,next_cell))
    return []
