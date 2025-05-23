
class d:
    def __init__(self, arr):
        self.arr = arr
        self.is_r = False

    def __iter__(self):
        if self.is_r:
            return reversed(self.arr)
        else:
            return iter(self.arr)
        
    def flip(self):
        self.is_r = not self.is_r

    def popleft(self):
        if self.arr:
            if self.is_r: self.arr.pop()
            else: self.arr.pop(0)
            return True
        else:
            return False
    def print(self):
        if len(self.arr) == 0:
            print("[]")
            return
        if self.is_r:
            print(f"[{self.arr[len(self.arr)-1]}", end="")
            for i in range(len(self.arr)-2, -1, -1):
                print(f",{arr[i]}", end="")
            print("]")
        else: 
            print(f"[{self.arr[0]}", end="")
            for i in range(1, len(self.arr)):
                print(f",{arr[i]}", end="")
            print("]")
tn = int(input())
for i in range(tn):
    inss = input()
    n = int(input())
    arr = input()
    arr = arr[1:-1]
    if arr == '':
        arr = []
    else: arr = list(map(int, arr.split(",")))
    deq = d(arr)
    is_err = False
    for ins in inss:
        if ins == 'R':
            deq.flip()
            # print(f"R: ")
            # deq.print()
        elif ins == 'D':
            if not deq.popleft():
                # print(f"D: ")
                # deq.print()
                is_err = True
                print("error")
                break
    if not is_err: deq.print()