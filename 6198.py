import sys
input = sys.stdin.readline
stk = []
n = int(input())

total = 0
for i in range(n):
    h = int(input())

    for j in range(len(stk)-1, -1, -1):
        if stk[j] > h:
            total += len(stk)
            break
        else:
            stk.pop()
    stk.append(h)

print(total)