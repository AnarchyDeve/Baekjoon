import sys
input = sys.stdin.readline

# 1. 입력
n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 2. 체스판 패턴과의 차이 기록 (왼쪽 위가 W인 체스판, B인 체스판)
diff_w = [[0] * m for _ in range(n)]  # W 시작 기준
diff_b = [[0] * m for _ in range(n)]  # B 시작 기준

for i in range(n):
    for j in range(m):
        # 현재 칸이 (i + j) 짝수 → 왼쪽 위와 같은 색이어야 함
        expected_w = 'W' if (i + j) % 2 == 0 else 'B'
        expected_b = 'B' if (i + j) % 2 == 0 else 'W'

        if board[i][j] != expected_w:
            diff_w[i][j] = 1
        if board[i][j] != expected_b:
            diff_b[i][j] = 1

# 3. 2D 누적합 만들기
def make_prefix_sum(diff):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (diff[i - 1][j - 1] +
                            prefix[i - 1][j] +
                            prefix[i][j - 1] -
                            prefix[i - 1][j - 1])
    return prefix

prefix_w = make_prefix_sum(diff_w)
prefix_b = make_prefix_sum(diff_b)

# 4. K x K 구간별로 최솟값 탐색
def get_sum(prefix, x1, y1, x2, y2):
    return (prefix[x2][y2] - prefix[x1 - 1][y2]
            - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])

min_change = float('inf')

for i in range(k, n + 1):
    for j in range(k, m + 1):
        change_w = get_sum(prefix_w, i - k + 1, j - k + 1, i, j)
        change_b = get_sum(prefix_b, i - k + 1, j - k + 1, i, j)
        min_change = min(min_change, change_w, change_b)

print(min_change)



######################################################3
#다른 사람 코드
import sys

N, M, K = map(int, sys.stdin.readline().split())

board = list(list(sys.stdin.readline().rstrip()) for _ in range(N))

def check(start_color):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for row in range(N):
        for col in range(M):
            if ((row + col) % 2 == 0):
                v = (board[row][col] != start_color)
            else:
                v = (board[row][col] == start_color)

            dp[row + 1][col + 1] = dp[row][col + 1] + dp[row + 1][col] - dp[row][col] + v

    MIN = N * M
    for row in range(1, N - K + 2):
        for col in range(1, M - K + 2):
            MIN = min(MIN, dp[row + K - 1][col + K - 1] - dp[row + K - 1][col - 1] - dp[row - 1][col + K - 1] + dp[row - 1][col - 1])

    return MIN

answer = min(check('B'), check('W'))
print(answer)