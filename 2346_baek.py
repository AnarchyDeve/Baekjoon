from collections import deque
import sys

num = int(sys.stdin.readline())
dq = deque(x for x in range(1, num + 1))
lst = deque(map(int, sys.stdin.readline().split()))
answer = []

while dq:
    answer.append(dq.popleft())  # 현재 위치에서 숫자 빼기
    if dq:  # dq가 남아 있을 때만 회전
        k = lst.popleft()
        dq.rotate(-(k - 1) if k > 0 else -k)
        lst.rotate(-(k - 1) if k > 0 else -k)

print(*answer)  # 리스트 형식이 아니라, 공백으로 출력
