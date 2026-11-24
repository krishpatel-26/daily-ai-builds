
def components(node_ids, lines):
    adjacency={id:set() for id in node_ids}
    for l in lines:
        adjacency[l.start].add(l.end)
        adjacency[l.end].add(l.start)
    components=[]
    remaining=set(node_ids)
    while remaining:
        origin=min(remaining)
        queue=[origin];remaining.remove(origin);comp=[]
        while queue:
            v=queue.pop();comp.append(v)
            for w in sorted(adjacency[v]):
                if w in remaining:
                    remaining.remove(w);queue.append(w)
        components.append(tuple(sorted(comp)))
    return sorted(components,key=lambda c:c[0])
