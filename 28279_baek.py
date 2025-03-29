import sys
from collections import deque

num = int(sys.stdin.readline())
dq = deque()
for i in range(num):
    x = list(map(int, sys.stdin.readline().split()))
    

    if x[0] == 1:
        dq.appendleft(x[1])
    elif x[0] == 2:
        dq.append(x[1])
    elif x[0] == 3:
        print(dq.popleft() if dq else -1)
    elif x[0] == 4:
        print(dq.pop () if dq else -1)
    elif x[0] == 5:
        print(len(dq))
    elif x[0] == 6:
        print(0 if dq else 1)
    elif x[0] == 7:
        print(dq[0] if dq else -1)
    elif x[0] == 8:
        print(dq[-1] if dq else -1)