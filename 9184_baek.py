import sys

sys.setrecursionlimit(100000)  # 재귀 깊이 초과 방지
input = sys.stdin.readline

# 메모이제이션을 위한 딕셔너리
dp = {}

def w(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        dp[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[(a, b, c)] = w(20, 20, 20)
    elif a < b and b < c:
        dp[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[(a, b, c)] = (
            w(a-1, b, c)
            + w(a-1, b-1, c)
            + w(a-1, b, c-1)
            - w(a-1, b-1, c-1)
        )
    return dp[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
