#1번쨰 풀이 위에서 아래로

import sys
sys.setrecursionlimit(10000)  # 깊은 재귀를 위해 필요할 수 있음

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
res = []

def dfs(row, col, total):
    if row == n:
        res.append(total)
        return
    dfs(row + 1, col, total + triangle[row][col])
    dfs(row + 1, col + 1, total + triangle[row][col])

dfs(0, 0, 0)
print(max(res))


#DP 문제풀이 방식 즉 아래에서 위로

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# 아래에서부터 위로 올라가며 값을 누적
for i in range(n - 2, -1, -1):        # 마지막 전 줄부터 0번째 줄까지
    for j in range(len(triangle[i])):  # 해당 줄의 각 원소에 대해
        # 현재 값 += 아래줄에서 선택 가능한 두 값 중 큰 것
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

# 맨 꼭대기에 최대값이 저장됨
print(triangle[0][0])
