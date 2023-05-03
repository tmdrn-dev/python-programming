# https://www.acmicpc.net/problem/2805
from sys import stdin

n, m = map(int, stdin.readline().split())
tree = sorted(list(map(int, stdin.readline().split())))

from bisect import bisect_left
h = 0

while h <= max(tree):
    start = bisect_left(tree, h)
    l = sum(list(map(lambda x: x-h, tree[start:])))
    # for i in tree[start:]:
    #     l += i-h
    if l == m:
        print(h)
        break
    elif l < m:
        print(h-1)
        break
    else:
        h += 1

    # print(start, h, l)
