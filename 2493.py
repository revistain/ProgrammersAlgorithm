import sys
input = sys.stdin.readline
n = int(input())

stk = []
ret = []
inp = list(map(int, input().split()))
idx = 0
for e in inp:
    t = 0
    for s in reversed(stk):
        if s[1] <= e:
            stk.pop()
        else:
            t = s[0]
            break
    idx += 1
    stk.append([idx, e])
    ret.append([idx, t])


for _ in ret:
    print(_[1])