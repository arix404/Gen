import heapq

n = int(input("Nodes: "))
graph = {i: [] for i in range(n)}

e = int(input("Edges: "))
for _ in range(e):
    u,v,w = map(int, input("u v w: ").split())
    graph[u].append((v,w))

start = int(input("Start node: "))

def dijkstra(start):
    dist = {i: float('inf') for i in graph}
    dist[start] = 0

    pq = [(0,start)]

    while pq:
        d,node = heapq.heappop(pq)

        for nei,w in graph[node]:
            if d+w < dist[nei]:
                dist[nei] = d+w
                heapq.heappush(pq,(dist[nei],nei))

    print(dist)

dijkstra(start)