from queue import PriorityQueue

goal = [1,2,3,4,5,6,7,8,0]

def heuristic(state):
    return sum([1 if state[i] != goal[i] else 0 for i in range(9)])

def astar(start):
    pq = PriorityQueue()
    pq.put((0, start, []))   # cost, state, path
    visited = set()

    while not pq.empty():
        cost, state, path = pq.get()

        if state == goal:
            print("\nSteps to Goal:")
            for step in path + [state]:
                print_state(step)
            return

        visited.add(tuple(state))

        for i in range(9):
            new = state[:]
            if i < 8:
                new[i], new[i+1] = new[i+1], new[i]
                if tuple(new) not in visited:
                    pq.put((heuristic(new), new, path + [state]))

def print_state(s):
    for i in range(0, 9, 3):
        print(s[i:i+3])
    print()

start = [1,2,3,4,5,6,0,7,8]
astar(start)