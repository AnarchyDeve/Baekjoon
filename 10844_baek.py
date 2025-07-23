n = int(input())
MOD = 1000000000

# dp[i][j] = i자리 계단수, 마지막 숫자 j
dp = [[0]*10 for _ in range(n+1)]

# 초기값 설정
for i in range(1, 10):
    dp[1][i] = 1

# DP 채우기
for i in range(2, n+1):       # 자릿수
    for j in range(10):       # 끝자리 숫자
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= MOD       # 나머지 처리

# 정답: n자리 수의 계단 수 개수의 총합
print(sum(dp[n]) % MOD)
