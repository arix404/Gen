import heapq

# -------------------- 1) 8-PUZZLE (A*) --------------------
def heuristic(state, goal):
    return sum(1 for i in range(9) if state[i] != goal[i])

def print_state(s):
    for i in range(0, 9, 3):
        print(s[i:i+3])
    print()

def get_moves(state):
    moves = []
    i = state.index(0)  # blank
    x, y = divmod(i, 3)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ni = nx*3 + ny
            new = state[:]
            new[i], new[ni] = new[ni], new[i]
            moves.append(new)
    return moves

def astar_puzzle():
    goal = list(map(int, input("Enter goal (9 nums): ").split()))
    start = list(map(int, input("Enter start (9 nums): ").split()))

    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()

    while pq:
        f, state, path = heapq.heappop(pq)

        if state == goal:
            print("\nSteps:")
            for s in path + [state]:
                print_state(s)
            return

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        for nxt in get_moves(state):
            if tuple(nxt) not in visited:
                g = len(path) + 1
                h = heuristic(nxt, goal)
                heapq.heappush(pq, (g+h, nxt, path + [state]))

    print("No solution")


# -------------------- 2) TIC-TAC-TOE (A*-style) --------------------
def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i] == b[j] == b[k] != ' ':
            return b[i]
    return None

def evaluate(board):
    winner = check_winner(board)
    if winner == 'X': return 10
    if winner == 'O': return -10
    return 0

def get_empty(board):
    return [i for i in range(9) if board[i] == ' ']

def astar_tictactoe():
    board = [' '] * 9
    print("Positions: 0-8")

    # take current board (optional simple input)
    for i in range(9):
        val = input(f"Enter position {i} (X/O/blank): ").strip().upper()
        if val in ['X','O']:
            board[i] = val

    pq = []
    heapq.heappush(pq, (-evaluate(board), board[:], []))  # maximize X

    visited = set()

    while pq:
        score, b, path = heapq.heappop(pq)

        winner = check_winner(b)
        if winner or ' ' not in b:
            print("\nBest sequence:")
            for step in path + [b]:
                print(step)
            return

        key = tuple(b)
        if key in visited:
            continue
        visited.add(key)

        for i in get_empty(b):
            new = b[:]
            new[i] = 'X'  # assume AI = X
            heapq.heappush(pq, (-evaluate(new), new, path + [b]))

    print("Done")


# -------------------- MENU --------------------
print("1. 8-Puzzle (A*)")
print("2. Tic-Tac-Toe (A*-style)")

choice = int(input("Enter choice: "))

if choice == 1:
    astar_puzzle()
elif choice == 2:
    astar_tictactoe()
else:
    print("Invalid choice")