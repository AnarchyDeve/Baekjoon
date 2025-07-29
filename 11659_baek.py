#시간 초과 처음 했을때 문제 

# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split())

# n_list = list(map(int, input().split()))

# for _  in range(m):
#     a, b = map(int, input().split())
#     res = n_list[a-1:b]
#     print(sum(res))

# 풀이 2 동적할당 사용버전

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 누적합 배열 만들기
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + n_list[i]

# 쿼리 처리
for _ in range(m):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])
