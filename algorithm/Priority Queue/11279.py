# https://www.acmicpc.net/board/view/11279

from sys import stdin
from heapq import heappush, heappop

n = int(stdin.readline())
num = list()
for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        if not num:
            print(0)
        else:
            print(heappop(num)[1])
    else:
        heappush(num, (-x, x))

