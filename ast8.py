
start = [

    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]

]


goal = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]

]


def find_zero(state):

    for i in range(3):

        for j in range(3):

            if state[i][j] == 0:
                return i, j

def h(state):

    count = 0

    for i in range(3):

        for j in range(3):

            if state[i][j] != 0 and state[i][j] != goal[i][j]:

                count += 1

    return count


# Print initial state
print("Initial State:")

for row in start:
    print(row)

print()



x, y = find_zero(start)


moves = [

    (-1,0),  # up
    (1,0),   # down
    (0,-1),  # left
    (0,1)    # right

]

best = start
best_h = h(start)

for dx, dy in moves:

    nx = x + dx
    ny = y + dy

    
    if 0 <= nx < 3 and 0 <= ny < 3:

        # Copy board
        temp = [row[:] for row in start]

        # Swap
        temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]

        # Calculate heuristic
        value = h(temp)

        # Choose best move
        if value < best_h:

            best_h = value
            best = temp


print("Next Best State:")

for row in best:
    print(row)

print()

print("Heuristic Value:", best_h)