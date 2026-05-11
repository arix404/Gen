
n = 4


graph = [

    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0]

]


start = 0


dist = [999] * n


dist[start] = 0


visited = [False] * n

for i in range(n):

    
    min_dist = 999
    u = -1

    for j in range(n):

        if not visited[j] and dist[j] < min_dist:

            min_dist = dist[j]
            u = j

    
    visited[u] = True

    
    for v in range(n):

        if graph[u][v] != 0 and not visited[v]:

            if dist[u] + graph[u][v] < dist[v]:

                dist[v] = dist[u] + graph[u][v]

print("Shortest distances:", dist)