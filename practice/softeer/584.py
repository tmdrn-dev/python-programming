# https://softeer.ai/practice/info.do?idx=1&eid=584

from sys import stdin

n, m = map(int, stdin.readline().split())

section = [list(map(int, stdin.readline().split())) for _ in range(n)]
test = [list(map(int, stdin.readline().split())) for _ in range(m)]

sp, tp = 0, 0
answer = 0

while tp < m:
    tl, ts = test[tp]
    sl, ss = section[sp]
    if sl <= 0:
        break

    if tl - sl > 0:
        test[tp] = [tl-sl, ts]
        section[sp] = [0, ss]
        answer = max(answer, ts-ss)
        sp += 1
    elif tl - sl < 0:
        test[tp] = [0, ts]
        section[sp] = [sl-tl, ss]
        answer = max(answer, ts-ss)
        tp += 1
    else:
        test[tp] = [0, ts]
        section[sp] = [0, ss]
        answer = max(answer, ts-ss)
        tp += 1
        sp += 1

print(answer)
