# https://www.acmicpc.net/problem/1927
from sys import stdin
from heapq import heappush, heappop

answer = list()
heap = list()
N = int(stdin.readline())
for _ in range(N):
    x = int(stdin.readline())
    if x > 0:
        heappush(heap, x)
    else:
        if heap:
            answer.append(heappop(heap))
        else:
            answer.append(0)

print(*answer)
