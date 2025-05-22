import sys
input = sys.stdin.readline

n = int(input())

# is popable?

# is right empty? => end / not found
# left의 Top에 있을 때까지 push
# end case: 못찾고 끝까지 갔을때, 

stk = []
ret = []
def check(elem):
    global stk
    return stk[-1] == elem

result = []
no_flag = False
num = 1
for j in range(n):
    target = int(input())
    if len(stk) == 0:
        stk.append(num)
        ret.append("+")
        num += 1
    while 100000:
        if stk[-1] > target or len(stk) == 0:
            no_flag = True
            break
        # 작다
        elif stk[-1] < target:
            stk.append(num)
            ret.append("+")
            num += 1
        # 같다
        else:
            stk.pop()
            ret.append("-")
            break

if not no_flag:
    for _ in ret:
        print(_)
else:
    print("NO")

        

