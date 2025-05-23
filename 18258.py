# 미완
import sys
input = sys.stdin.readline

n = int(input())

queue = [0 for i in range(2000000)]
index = 0
iend = 0
ret = []
for i in range(n):
    inp = list(map(str, input().split()))
    if len(inp) == 2:
        queue[iend] = inp[1]
        iend += 1
    else:
        if inp[0] == "pop":
            if index != iend:
                print(queue[index])
                index += 1
            else: print(-1)
        elif inp[0] == "size":
            print(iend - index)
        elif inp[0] == "empty":
            if index != iend: print(0)
            else: print(1)
        elif inp[0] == "front":
            if index != iend: print(queue[index])
            else: print(-1)
        elif inp[0] == "back":
            if index != iend: print(queue[iend-1])
            else: print(-1)
