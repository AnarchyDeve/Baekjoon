import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

res = 0

def jump(idx, step, total):
    global res
    if idx >= n:
        return
    if idx == n - 1:
        res = max(res, total + s[idx])
        return
    
    # 한 칸 오르기 (step+1)
    if step < 2:
        jump(idx + 1, step + 1, total + s[idx])
    
    # 두 칸 오르기 (step 리셋)
    jump(idx + 2, 1, total + s[idx])

# 시작점은 idx=0 또는 idx=1로 시도할 수 있음
jump(0, 1, 0)  # 0번째 계단에서 시작
res = max(res, 0)  # 아무것도 안 밟은 경우도 고려
print(res)


### 동적할당 방법
import sys

input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]  # 각 계단의 점수

# 예외 처리: 계단이 1개 또는 2개일 경우
if n == 1:
    print(s[0])
elif n == 2:
    print(s[0] + s[1])
else:
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0] + s[2], s[1] + s[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

    print(dp[-1])

