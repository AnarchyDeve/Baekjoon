import collections

num = int(input())
lst = collections.deque([i for i in range(1, num+1)])
while len(lst) > 1:
    lst.popleft()
    a = lst.popleft()
    lst.append(a)

print(lst[0])