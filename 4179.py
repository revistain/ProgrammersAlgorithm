from collections import deque
from enum import Enum
import sys
input = sys.stdin.readline

class Type(Enum):
    wall = 0
    fire = 1
    safe = 2
    jihoon = 3

deq = deque()
row, col = map(int, input().split())
maze = [[0 for _ in range(col)] for _ in range(row)]
for r in range(row):
    inp = input()
    for c in range(col):
        con = inp[c]
        if con == "#": maze[r][c] = Type.wall
        elif con == "F":
            maze[r][c] = Type.fire
            deq.append([r, c, 0])
        elif con == ".": maze[r][c] = Type.safe
        elif con == "J": maze[r][c] = Type.jihoon

escaped = False
while deq:
    rcl = deq.pop()
    r = rcl[0]
    c = rcl[1]
    l = rcl[2]
    if r == 0 or c == 0 or r == row-1 or c == col-1:
        escaped = True
        break

    if c != 0 and maze[r][c-1] == Type.safe:
        maze[r][c-1] = Type.fire
        deq.append([r, c-1, l+1])
    if c < col-1 and maze[r][c+1] == Type.safe:
        maze[r][c-1] = Type.fire
        deq.append([r, c+1, l+1])
    if r != 0 and maze[r-1][c] == Type.safe:
        maze[r][c-1] = Type.fire
        deq.append([r-1, c, l+1])
    if r < row - 1 and maze[r+1][c] == Type.safe:
        maze[r][c-1] = Type.fire
        deq.append([r+1, c, l+1])


for r in range(row):
    for c in range(col):
        print(maze[c][r], "", end="")
    print()