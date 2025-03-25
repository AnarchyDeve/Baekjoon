def check(lst):
    count = 0
    for i in lst:
        if i == '(':
            count +=1
        elif i == ')':            
            count -=1
        if count < 0:
            print('NO')
            return
    if count == 0:
        print('YES')
    else:
        print('NO')


num = int(input())

for _ in range(num):
    lst = list(input())
    check(lst)
