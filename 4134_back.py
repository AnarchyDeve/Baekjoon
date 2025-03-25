def isPrime(n):
    if n < 2 : return False
    if n == 2: return True 
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input())

for _ in range(num):
    n = int(input())
        
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1