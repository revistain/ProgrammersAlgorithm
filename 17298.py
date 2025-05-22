import sys
input = sys.stdin.readline

n = int(input())
inp = list(map(int, input().split()))

stk = []
ret = {}
for i in range(n):
    t = inp[i]
    
    for s in reversed(stk):
        if s[1] < t:
            popped = stk.pop()
            ret[s[0]] = t
        else:
            break
    stk.append([i, t])

for i in range(n):
    if i in ret: print(ret[i])
    else: print("-1")
