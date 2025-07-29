# 1번째 풀이 

# import sys

# input = sys.stdin.readline

# sen = input()
# n = int(input())

# for _ in range(n):
#     f, s, e = input().split()
#     s, e = int(s), int(e)
#     count = 0

#     for i in range(s, e + 1):
#         if f == sen[i]:
#             count += 1
#     print(count)


# 2번째 풀이 딕셔너리 + 찾기 이것 또한 50점이 나옴

# import sys
# input = sys.stdin.readline

# from collections import defaultdict

# sen = input().strip()
# n = int(input())

# # 알파벳 → 등장 인덱스 리스트 저장
# char_pos = defaultdict(list)
# for idx, ch in enumerate(sen):
#     char_pos[ch].append(idx)

# # 쿼리 처리
# for _ in range(n):
#     f, s, e = input().split()
#     s, e = int(s), int(e)

#     count = 0
#     for idx in char_pos[f]:
#         if s <= idx <= e:
#             count += 1
#     print(count)


import sys

s = sys.stdin.readline().rstrip()
count = {0 : [0] * 26}

q = int(sys.stdin.readline().rstrip())
for i, ch in enumerate(s):
    count[i + 1] = count[len(count) - 1][:]
    count[i + 1][ord(ch) - 97] += 1

for _ in range(q):
    alpha, l, r = sys.stdin.readline().rstrip().split()
    answer = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]
    print(answer)