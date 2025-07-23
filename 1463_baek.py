# import sys

# input = sys.stdin.readline

# n = int(input().strip())
# count = 0

# def op(n):        
#     global count
#     if n == 1:
#         return
#     count += 1
#     if n % 3 == 0:
#         op(n//3)
#     elif (n-1) % 3 == 0:
#         op(n - 1)
#     elif n % 2 == 0:
#         op(n//2)
#     else:
#         op(n - 1)

# op(n)
# print(count)
import sys  # 빠른 입력을 위한 sys 모듈 불러오기

input = sys.stdin.readline  # 입력 속도 향상을 위해 input 함수를 sys.stdin.readline으로 재정의
n = int(input())  # 사용자로부터 정수 n 입력 받기

dp = [0] * (n + 1)  # dp[i]: i를 1로 만들기 위한 최소 연산 횟수를 저장하는 리스트 (0~n까지 총 n+1개)

# 2부터 n까지 반복하면서 dp 테이블 채우기
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 기본 연산: i - 1에서 1을 더해서 i를 만든 경우 (+1은 연산 하나 수행했다는 의미)

    if i % 2 == 0:  # i가 2로 나누어 떨어진다면
        dp[i] = min(dp[i], dp[i // 2] + 1)  # i를 2로 나눠서 만든 경우도 고려하여 더 작은 값으로 갱신

    if i % 3 == 0:  # i가 3으로 나누어 떨어진다면
        dp[i] = min(dp[i], dp[i // 3] + 1)  # i를 3으로 나눠서 만든 경우도 고려하여 더 작은 값으로 갱신

# 최종적으로 n을 1로 만드는 데 필요한 최소 연산 횟수 출력
print(dp[n])

