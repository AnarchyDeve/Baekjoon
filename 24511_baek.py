from collections import deque

int(input())
qns = list(map(int, input().split()))
init = list(map(int, input().split()))

int(input())
values = list(map(int, input().split()))

d = deque([init[i] for i in range(len(qns)) if qns[i] == 0])

for i in values:
    d.appendleft(i)
    print(d.pop(), end=' ')