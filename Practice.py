import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    n = int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n += 1

def check(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True