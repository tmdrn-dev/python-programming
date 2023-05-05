# https://www.acmicpc.net/problem/2805
from sys import stdin

n, m = map(int, stdin.readline().split())
tree = sorted(list(map(int, stdin.readline().split())))
start, end = 1, max(tree)

while start <= end:
    mid = int((start+end)/2)

    l = 0
    for i in tree:
        if i >= mid:
            l += i-mid
    if l >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
