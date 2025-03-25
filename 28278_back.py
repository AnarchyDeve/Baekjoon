import sys

lst = []
n = sys.stdin.readline()
n = int(n)
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        lst.append(int(command[1]))
    elif command[0] == '2':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop()) 
    elif command[0] == '3':
        print(len(lst))
    elif command[0] == '4':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == '5':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])