# https://www.acmicpc.net/problem/2352
# https://seungkwan.tistory.com/8

from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
port = list(map(int, stdin.readline().split()))
L = list()
P = list()
element = list()

# length of longest subsequence
for i, j in enumerate(port):
    if not L or L[-1] < j:
        L.append(j)
        P.append(L.index(j))
    else:
        L[bisect_left(L, j)] = j
        P.append(L.index(j))

# answer
print(len(L))
# print(L)
# print(P)

# element of longest subsequence
length = len(L)-1
for i, j in reversed(list(enumerate(P))):
    if j is length:
        element.append(port[i])
        length -= 1

#print(*reversed(element))