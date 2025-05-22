from sys import stdin
st = [0] * 10000
idx = 0
output_result = []

def push(elem):
    global st, idx
    st[idx] = int(elem)
    idx += 1

def empty():
    if idx == 0: return 1
    else: return 0

def pop():
    global st, idx
    idx -= 1
    return str(st[idx])

def size():
    global st, idx
    return idx

def top():
    global st, idx
    return str(st[idx-1])

n = int(stdin.readline())
for i in range(n):
    opcode = list(map(str, stdin.readline().split()))
    if len(opcode) == 1:
        if opcode[0] == "top":
            if empty(): output_result.append("-1")
            else: output_result.append(top())
        elif opcode[0] == "size":
            output_result.append(size())
        elif opcode[0] == "empty":
            output_result.append(1) if empty() else output_result.append(0)
        elif opcode[0] == "pop":
            output_result.append(-1) if empty() else output_result.append(pop())
    elif len(opcode) == 2:
        if opcode[0] == "push":
            push(opcode[1])

print(output_result)