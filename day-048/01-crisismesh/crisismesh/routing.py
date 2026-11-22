import heapq

def route(water, start, goal, max_water=4, policy='risk_aware'):
    height=len(water); width=len(water[0]); start=tuple(start);goal=tuple(goal)
    if policy not in ('risk_aware','shortest'): raise ValueError('unknown route policy')
    if not (0<=start[0]<width and 0<=start[1]<height and 0<=goal[0]<width and 0<=goal[1]<height): return None
    if water[goal[1]][goal[0]]>max_water or water[start[1]][start[0]]>max_water:return None
    heap=[(0.0, start)];cost={start:0.0};prev={}
    while heap:
        g,p=heapq.heappop(heap)
        if g>cost[p]+1e-9:continue
        if p==goal:
            path=[p]
            while p in prev:p=prev[p];path.append(p)
            return {'path':[list(x) for x in path[::-1]], 'cost':round(g,3), 'steps':len(path)-1}
        for q in ((p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)):
            x,y=q
            if not (0<=x<width and 0<=y<height) or water[y][x]>max_water: continue
            step=1.0+(0.95*water[y][x] if policy=='risk_aware' else 0)
            ng=g+step
            if ng<cost.get(q,float('inf')):
                cost[q]=ng;prev[q]=p;heapq.heappush(heap,(ng,q))
    return None