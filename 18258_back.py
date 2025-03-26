import sys
from collections import deque

N = int(sys.stdin.readline())
DQ = deque()
for _ in range(N):
    S = sys.stdin.readline().split()

    if S[0] == 'push':  # 정수 X를 큐에 넣는다.
        DQ.append(int(S[1]))

    if S[0] == 'pop':   # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다
        if DQ:   # Q 안에 값이 존재하는 경우
            print(DQ.popleft())
        else:
            print(-1)

    if S[0] == 'size':  # 큐에 들어있는 정수의 개수를 출력한다.
        print(len(DQ))

    if S[0] == 'empty':
        if DQ:
            print('0')
        else:
            print('1')

    if S[0] == 'front':
        if DQ:
            print(DQ[0])
        else:
            print(-1)

    if S[0] == 'back':
        if DQ:
            print(DQ[-1])
        else:
            print(-1)