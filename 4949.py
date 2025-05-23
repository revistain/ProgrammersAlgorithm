import sys
input = sys.stdin.readline

while True:
    line = input()
    if line[0] == ".": break
    stk = []
    no_flag = False
    for c in line:
        if c == "(" or c == "[":
            stk.append(c)
        elif c == ")":
            if not stk:
                no_flag = True
                break
            top = stk.pop()
            if top != "(":
                no_flag = True
                break
        elif c == "]":
            if not stk:
                no_flag = True
                break
            top = stk.pop()
            if top != "[":
                no_flag = True
                break
    
    if stk:
        no_flag = True
    if no_flag: print("no")
    else: print("yes")