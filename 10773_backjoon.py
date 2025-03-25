import sys

n = sys.stdin.readline()
lst = []
for _ in range(int(n)):
    num = sys.stdin.readline().strip()
    if num == '0':
        lst.pop()
    else:
        lst.append(num)

print(sum(map(int,lst)))
    