import sys
input = sys.stdin.readline

n = int(input())

# 재귀 방식
count1 = 0
def fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# DP 방식
def fibonacci_dp(n):
    count2 = 0
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count2 += 1
    return count2

fib(n)
print(count1, end= ' ')
print(fibonacci_dp(n))
