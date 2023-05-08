# https://www.acmicpc.net/board/view/110871

from sys import stdin
from heapq import heappush, heappop

n = int(stdin.readline())
st = list()
for _ in range(n):
    s, t = map(int, stdin.readline().split())
    heappush(st, (s,t))

s, t = heappop(st)
heap = [t]
while st:
    s, t = heappop(st)
    if not heap:
        heappush(heap, t)
    if s >= heap[0]:
        heappop(heap)
    heappush(heap, t)

print(len(heap))