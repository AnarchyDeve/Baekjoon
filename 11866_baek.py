import collections

n,k = map(int, input().split())
dq = collections.deque(i for i in range(1, n+1))
answer = []

while dq:
    dq.rotate(-k+1)
    answer.append(dq.popleft())
print('<',', '.join(map(str, answer)),'>', sep = '')

