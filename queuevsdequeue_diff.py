import queue
from collections import deque
import time

# 테스트할 데이터 크기
N = 1000000

# queue.Queue() 속도 테스트
q = queue.Queue()
start = time.time()
for i in range(N):
    q.put(i)
for i in range(N):
    q.get()
print("queue.Queue() 실행 시간:", time.time() - start)

# collections.deque 속도 테스트
dq = deque()
start = time.time()
for i in range(N):
    dq.append(i)
for i in range(N):
    dq.popleft()
print("collections.deque 실행 시간:", time.time() - start)
