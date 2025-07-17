import sys

input = sys.stdin.readline
memo = {0:0,1: 1, 2:1, 3:1}

def pado(n):
    if n in memo:
        return memo[n]
    else:     
        memo[n] = pado(n-2) + pado(n-3)
        return memo[n]
    
#main 문
n = int(input())
for _ in range(n):
    print(pado(int(input())))
