# import sys

# n = int(sys.stdin.readline())
# sen = '-'
# for _ in range(n):
#     result = ''
#     for i in sen:
#         if i == '-':
#             result += '- -'
#         else:
#             result += '   '

#     sen = result
# print(sen)

import sys

def cantor(n):
    if n == 0:
        return '-'
    prev = cantor(n - 1)
    return prev + ' ' * (3**(n - 1)) + prev

for line in sys.stdin:
    n = int(line.strip())
    print(cantor(n))
