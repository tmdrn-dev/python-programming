# https://softeer.ai/practice/info.do?idx=1&eid=395

from sys import stdin

w, n = map(int, stdin.readline().split())
mp = list(tuple(map(int, stdin.readline().split())) for _ in range(n))
mp.sort(key=lambda x: x[1], reverse=True)

price = 0
for m, p in mp:
    if w == 0:
        break

    if w-m >= 0:
        price += m*p
        w -= m
    elif w-m < 0:
        price += w*p
        w = 0

print(price)
