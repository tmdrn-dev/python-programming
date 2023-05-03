# https://www.acmicpc.net/problem/2805
from sys import stdin

n, m = map(int, stdin.readline().split())
tree = sorted(list(map(int, stdin.readline().split())))

from bisect import bisect_left
h = tree[int(n/2)]

while h < max(tree):
    l = 0
    start = bisect_left(tree, h)
    for i in tree[start:]:
        l += i-h
    if l == m:
        print(h)
        break
    elif l > m:
        h += 1
    else:
        h -= 1

    # print(start, h, l)
