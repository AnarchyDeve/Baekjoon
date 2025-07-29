# 행마다 누적합을 구하고, 각 행의 누적합을 이용해 구간 합을 계산하는 방식 
## 시간 초과가 떠서 틀렸음

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 행별 누적합 배열 만들기 (row_prefix[i][j]는 0 ~ j-1까지의 합)
row_prefix = [[0] * (n + 1) for _ in range(n + 1)]  # 1-based 인덱스

for i in range(1, n + 1):  # 행
    for j in range(1, n + 1):  # 열
        row_prefix[i][j] = row_prefix[i][j - 1] + arr[i - 1][j - 1]

# 2. 질의 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for row in range(x1, x2 + 1):
        res += row_prefix[row][y2] - row_prefix[row][y1 - 1]
    print(res)

# 2번째 풀이: 누적합 배열을 이용한 구간 합 계산(사각형의 합을 구해서 하는 방식)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 누적합 배열: dp[i][j]는 (1,1) ~ (i,j)까지의 합
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = (
            arr[i - 1][j - 1]
            + dp[i - 1][j]
            + dp[i][j - 1]
            - dp[i - 1][j - 1]
        )

# 쿼리 처리
for _ in range(m):
    a1, a2, b1, b2 = map(int, input().split())

    res = (
        dp[b1][b2]
        - dp[a1 - 1][b2]
        - dp[b1][a2 - 1]
        + dp[a1 - 1][a2 - 1]
    )

    print(res)
