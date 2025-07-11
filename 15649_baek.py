import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

n_list = [x for x in range(1, n + 1)]
k = list(itertools.permutations(n_list, m))  # m으로 바꾸는게 자연스러워 보임

for i in k:
    print(' '.join(map(str, i)))
