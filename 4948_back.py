#실패한 풀이

# def check(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, int(n**0.5)+1):
#             if n % i ==0:
#                 return False
#         lst.append(n)
#         n_set.add(n)
        

# running = True

# while running:
#     n = int(input())
#     lst = []
#     n_set = set()

#     if n == 0:
#         break
#     for j in range(n+1, 2*n+1):
#         if j not in n_set:
#             check(j)
#     print(len(lst))
#     lst.clear()

lst = [0] *2 + [1] * 123455
for i in range(2, int(123456**0.5) +1):
    m = 123456 // i 
    if lst[i] == 0:
        continue
    for j in range(2, m+1):
        lst[i*j] = 0

while True:
    x = int(input())
    if x ==0:
        break
    print(sum(lst[x+1:x*2+1]))