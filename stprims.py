# Adjacency matrix

graph = [

    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]

]

n = 4

visited = [0] * n

# Start from node 0
visited[0] = 1

print("Edges in MST:")

for i in range(n - 1):

    min = 999

    for j in range(n):

        if visited[j]:

            for k in range(n):

                if graph[j][k] != 0 and not visited[k]:

                    if graph[j][k] < min:

                        min = graph[j][k]

                        a = j
                        b = k

    print(a, "-", b, "=", min)

    visited[b] = 1

#o(v2)