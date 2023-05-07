# https://www.acmicpc.net/problem/15829

from sys import stdin
L = int(stdin.readline())
S = stdin.readline().strip()

answer = 0
for i, s in enumerate(S):
    answer += (ord(s)%96)*31**i

print(answer%1234567891)
