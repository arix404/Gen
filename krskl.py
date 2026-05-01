n = int(input("Nodes: "))
e = int(input("Edges: "))

edges = []
for _ in range(e):
    u,v,w = map(int, input("u v w: ").split())
    edges.append((w,u,v))

edges.sort()

parent = {i:i for i in range(n)}

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    parent[find(x)] = find(y)

for w,u,v in edges:
    if find(u)!=find(v):
        print(u,v,w)
        union(u,v)