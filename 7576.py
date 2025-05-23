from collections import deque
import sys
input = sys.stdin.readline

def findNear(c, r, cc, cr):
    near = []
    if cc != 0:
        near.append("left")
    if cr != 0:
        near.append("up")
    if cc < c-1:
        near.append("right")
    if cr < r-1:
        near.append("down")

    return near

gc, gr = map(int, input().split())
spos = []
box = [[0 for _ in range(gr)] for _ in range(gc)]
box_check = [[0 for _ in range(gr)] for _ in range(gc)]
box_level = [[-1 for _ in range(gr)] for _ in range(gc)]
for row in range(gr):
    inp = list(map(int, input().split()))
    for col in range(gc):
        box[col][row] = inp[col]
        if inp[col] == 1:
            spos.append([col, row])

deq = deque()

for _ in spos:
    deq.append(_)
    box_check[_[0]][_[1]] = 1
    box_level[_[0]][_[1]] = 0

max_lv = 0
while deq:
    [c, r] = deq.popleft()
    if box_level[c][r] > max_lv:
        max_lv = box_level[c][r]
    # print("popped : ", c, r)
    nears = findNear(gc,gr,c,r)
    # print("nears", nears)
    if "up" in nears and box_check[c][r-1] == 0 and box[c][r-1] != -1:
        # print("append left")
        deq.append([c, r-1])
        box_check[c][r-1] = 1
        box_level[c][r-1] = box_level[c][r] + 1
    if "left" in nears and box_check[c-1][r] == 0 and box[c-1][r] != -1:
        # print("append up")
        deq.append([c-1, r])
        box_check[c-1][r] = 1
        box_level[c-1][r] = box_level[c][r] + 1
    if "down" in nears and box_check[c][r+1] == 0 and box[c][r+1] != -1:
        # print("append right")
        deq.append([c, r+1])
        box_check[c][r+1] = 1
        box_level[c][r+1] = box_level[c][r] + 1
    if "right" in nears and box_check[c+1][r] == 0 and box[c+1][r] != -1:
        # print("append down")
        deq.append([c+1, r])
        box_check[c+1][r] = 1
        box_level[c+1][r] = box_level[c][r] + 1
    
    # for r in range(gr):
    #     for c in range(gc):
    #         print(box_level[c][r],"", end="")
    #     print()

flag = False
for row in range(gr):
    for col in range(gc):
        if box_level[col][row] == -1 and box[col][row] != - 1:
            flag = True

if flag: print("-1")
else: print(max_lv)