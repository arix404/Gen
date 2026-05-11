# Edges: (weight, node1, node2)

edges = [

    (2, 0, 1),
    (3, 1, 2),
    (6, 0, 3),
    (8, 1, 3)

]

# Sort edges
edges.sort()

parent = [0, 1, 2, 3]

print("Edges in MST:")

for w, u, v in edges:

    if parent[u] != parent[v]:

        print(u, "-", v, "=", w)

        old = parent[v]

        for i in range(len(parent)):

            if parent[i] == old:

                parent[i] = parent[u]


#o(eloge)