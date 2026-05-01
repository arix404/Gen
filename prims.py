import heapq

n = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(n)}

e = int(input("Enter number of edges: "))
for _ in range(e):
    u,v,w = map(int, input("u v weight: ").split())
    graph[u].append((w,v))
    graph[v].append((w,u))

start = int(input("Start node: "))

def prim(start):
    visited = set([start])
    edges = graph[start]
    heapq.heapify(edges)

    while edges:
        w, v = heapq.heappop(edges)
        if v not in visited:
            print(f"{start}-{v} = {w}")
            visited.add(v)
            for edge in graph[v]:
                heapq.heappush(edges, edge)

prim(start)