# import sys

# input = sys.stdin.readline

# n = int(input())
# s = list(map(int, input().strip().split()))
# res = []

# # 양수가 하나도 없으면 최대값 출력 후 종료
# if not any(x > 0 for x in s):
#     print(max(s))

# else:  
#     count = 0
#     for i in range(0, len(s)):  # 1부터 시작해서 s[i]만 접근
#         if s[i] >= 0:
#             count += s[i]
#         else:
#             res.append(count)
#             res.append(s[i]) #음수도 넣어
#             count = 0
#     res.append(count)  # 마지막 양수 구간 추가


# #그리고 res를 순회하면서 슬라이싱해보면서 max값을 찾아 이방식은 문제가 있으니 아래 방식으로 하는게 깔끔함

import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().strip().split()))

if not any(x > 0 for x in s):
    print(max(s))


else:
    max_sum = current_sum = 0

    for i in range(0, n):
        current_sum = max(s[i], current_sum + s[i]) #여기 max안에 current_sum이 음수면 0이다가 녹아있음
        max_sum = max(max_sum, current_sum)

    print(max_sum)
