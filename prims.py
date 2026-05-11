graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):

    u, v, w = map(int, input("Enter u v w: ").split())

    graph[u].append((v, w))
    graph[v].append((u, w))

visited = []

start = int(input("Enter starting node: "))

visited.append(start)

print("Edges in MST:")

while len(visited) < n:

    min_edge = [None, None, 9999]

    for node in visited:

        for neighbour, weight in graph[node]:

            if neighbour not in visited:

                if weight < min_edge[2]:

                    min_edge = [node, neighbour, weight]

    print(min_edge[0], "-", min_edge[1], "=", min_edge[2])

    visited.append(min_edge[1])