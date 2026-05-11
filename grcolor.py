n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

color = [0] * n

def safe(v, c):

    for i in range(n):

        if graph[v][i] == 1 and color[i] == c:
            return False

    return True

def solve(v):

    if v == n:
        print("Solution:", color)
        return True

    for c in range(1, m+1):

        if safe(v, c):

            color[v] = c

            if solve(v+1):
                return True

            color[v] = 0

    return False

solve(0)