import sys
input = sys.stdin.readline

sen1 = input().strip()
sen2 = input().strip()

n = len(sen1)
m = len(sen2)

# dp[i][j]: sen1의 i번째 문자까지, sen2의 j번째 문자까지의 LCS 길이
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if sen1[i - 1] == sen2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])  # 최종 결과


#문제를 처음 읽었을떄 4개의 종류와 K 까지 할수 있다고 하면 13 /  6 등 가치가 무게당 가치가 가장 높은걸로 계속 채워넣으면 되는거 아니야?