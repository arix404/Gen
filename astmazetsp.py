import heapq

# -------------------- COMMON --------------------
def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# -------------------- 1) MAZE (A*) --------------------
def astar_maze():
    n = int(input("Rows: "))
    m = int(input("Cols: "))
    print("Enter grid (0=free, 1=block):")
    grid = [list(map(int, input().split())) for _ in range(n)]

    sx, sy = map(int, input("Start (x y): ").split())
    gx, gy = map(int, input("Goal (x y): ").split())

    pq = []
    heapq.heappush(pq, (0, (sx, sy), []))  # (f, node, path)
    visited = set()

    while pq:
        f, (x, y), path = heapq.heappop(pq)

        if (x, y) == (gx, gy):
            print("\nPath:")
            for p in path + [(x, y)]:
                print(p, end=" ")
            print()
            return

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                g = len(path) + 1
                h = manhattan((nx, ny), (gx, gy))
                heapq.heappush(pq, (g+h, (nx, ny), path + [(x, y)]))

    print("No path found")

# -------------------- 2) TSP (A* style) --------------------
def astar_tsp():
    n = int(input("Number of cities: "))
    print("Enter cost matrix:")
    cost = [list(map(int, input().split())) for _ in range(n)]

    start = 0
    pq = []
    heapq.heappush(pq, (0, start, [start], 0))  
    # (f, current_city, path, g_cost)

    while pq:
        f, city, path, g = heapq.heappop(pq)

        if len(path) == n:
            total_cost = g + cost[city][start]
            print("\nTour:", path + [start])
            print("Cost:", total_cost)
            return

        for next_city in range(n):
            if next_city not in path:
                new_g = g + cost[city][next_city]
                h = 0  # simple heuristic (can say "0 for simplicity")
                heapq.heappush(pq, (new_g + h, next_city, path + [next_city], new_g))

# -------------------- MENU --------------------
print("1. Maze Pathfinding (A*)")
print("2. Travelling Salesman Problem (A*)")

choice = int(input("Enter choice: "))

if choice == 1:
    astar_maze()
elif choice == 2:
    astar_tsp()
else:
    print("Invalid choice")