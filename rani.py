N = int(input("Enter N: "))
board = [[0]*N for _ in range(N)]

def safe(r,c):
    for i in range(c):
        if board[r][i]: return False
    for i,j in zip(range(r,-1,-1), range(c,-1,-1)):
        if board[i][j]: return False
    for i,j in zip(range(r,N), range(c,-1,-1)):
        if board[i][j]: return False
    return True

def solve(c):
    if c>=N:
        for row in board:
            print(row)
        return True

    for i in range(N):
        if safe(i,c):
            board[i][c]=1
            if solve(c+1): return True
            board[i][c]=0
    return False

solve(0)