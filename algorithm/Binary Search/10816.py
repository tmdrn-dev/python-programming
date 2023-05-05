from sys import stdin

n = int(stdin.readline())
cards = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))
answer = list()

from bisect import bisect_left, bisect_right

for target in targets:
    li = bisect_left(cards, target)
    ri = bisect_right(cards, target)

    answer.append(ri-li)

print(*answer)