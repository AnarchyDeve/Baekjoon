import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = 0
count = [0] * m
count[0] = 1  # prefix % m == 0 일 경우를 위한 초기값

answer = 0
for num in arr:
    prefix += num
    mod = prefix % m
    answer += count[mod]
    count[mod] += 1

print(answer)
