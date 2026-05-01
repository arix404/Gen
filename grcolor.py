n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

color = [0] * n   # stores color of each vertex

def is_safe(v, c):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve(v):
    if v == n:
        print("\nSolution (Color Assignment):", color)
        return True

    for c in range(1, m + 1):
        print(f"Trying color {c} for vertex {v}")   # shows working
        if is_safe(v, c):
            color[v] = c
            print(f"Assigned color {c} to vertex {v}")

            if solve(v + 1):
                return True

            print(f"Backtracking on vertex {v}")
            color[v] = 0   # undo

    return False

if not solve(0):
    print("No solution found")