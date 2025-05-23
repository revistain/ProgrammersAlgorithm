import sys
input = sys.stdin.readline

n ,w = map(int, input().split())
inp = list(map(int, input().split()))

s = set()
ret = []
cnt = {}
for i in range(-w+1, n-w+1):
    if i-1 >= 0:
        val = inp[i-1]
        if val in cnt:
            if cnt[val] > 1:
                cnt[val] -= 1
            else:
                cnt[val] = 0
                s.remove(val)
    if i < n:
        val = inp[i+w-1]
        if val in cnt:
            cnt[val] += 1
        else: cnt[val] = 1

        s.add(val)
    print(s)
    ret.append(next(iter(s)))

for _ in ret:
    print(_, "", end="")