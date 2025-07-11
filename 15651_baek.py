import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
n_list = [x for x in range(1, n+1)]

k = list(itertools.product(n_list, repeat = m))

for i in k:
    print(" ".join(map(str, i)))

