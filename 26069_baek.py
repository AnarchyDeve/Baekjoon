import sys

n = int(sys.stdin.readline().strip())
n_list = ['ChongChong']

for _ in range(n):
    a,b = sys.stdin.readline().strip().split()

    if a in n_list or b in n_list:
        n_list.append(a)
        n_list.append(b)
    
print(len(set(n_list)))