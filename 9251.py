import sys

input = sys.stdin.readline

sen1 = input().strip()
sen1_copy = sen1
sen2 = input().strip()
sen2_copy = sen2
res1 = []
res2 = []
for i in sen1:
    if sen2_copy.find(i):
        res1.append()