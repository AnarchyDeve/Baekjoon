n = int(input())
lst_1 = list(map(int, input().split()))
stack = []
check = 1

for i in lst_1:
    if i == check:
        check += 1
    else:
        stack.append(i)

    while stack and stack[-1] == check:
        stack.pop()
        check += 1

if not stack:
    print("Nice")
else:
    print("Sad")
