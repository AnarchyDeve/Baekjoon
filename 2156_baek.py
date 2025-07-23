import sys
input = sys.stdin.readline

n = int(input())
wine = [0]  # 인덱스 맞추기 위해 앞에 dummy 0 추가

for _ in range(n):
    wine.append(int(input()))

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
else:
    dp = [0] * (n + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]

    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],                            # 현재 잔 안 마시는 경우
            dp[i - 2] + wine[i],                 # 이전 잔은 안 마신 경우
            dp[i - 3] + wine[i - 1] + wine[i]    # 전전 잔 안 마신 경우
        )

    print(dp[n])
