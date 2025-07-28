import sys

input = sys.stdin.readline
n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]

# A 전봇대 기준 정렬
x.sort(key=lambda x: x[0])

# LIS 구하기 (B 전봇대 기준)
lst = [1] * n  # 초기값을 1로 설정해야 함!

for i in range(n):
    for j in range(i):
        if x[i][1] > x[j][1]:
            lst[i] = max(lst[i], lst[j] + 1)

print(n - max(lst))  # 전체에서 LIS 길이만큼 남기면 나머지는 제거
