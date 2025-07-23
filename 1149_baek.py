# from itertools import permutations
# import sys

# input = sys.stdin.readline
# n = int(input())

# number = list(permutations(range(n), n))

# house = []
# for _ in range(n):
#     house.append(list(map(int, input().split())))
# print(house)
# res = []

# for i,j in enumerate(number):
#     money = 0
#     for p,q in enumerate(j):
#         money += house[p][q]
#     res.append(money)

# print(min(res)) # 102 를 건드리면 1은 0,0이고 

### 메모리 초과가 떳음
# from itertools import product
# import sys

# input = sys.stdin.readline
# n = int(input())

# # 모든 조합 생성 (중복 허용, 각 자리에 0~n-1)
# number = list(product(range(n), repeat=n))

# # 연속된 숫자가 같은 경우 제거
# filtered = [case for case in number if all(case[i] != case[i+1] for i in range(n - 1))]

# # 집 비용 입력
# house = [list(map(int, input().split())) for _ in range(n)]

# res = []

# for j in filtered:
#     money = 0
#     for p, q in enumerate(j):
#         money += house[p][q]
#     res.append(money)

# print(min(res))

#정답코드

import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블: house[i][색상]에다가 누적 최소 비용을 덮어씌움
for i in range(1, n):
    house[i][0] += min(house[i-1][1], house[i-1][2])  # 빨강
    house[i][1] += min(house[i-1][0], house[i-1][2])  # 초록
    house[i][2] += min(house[i-1][0], house[i-1][1])  # 파랑

print(min(house[n-1]))
