# https://www.acmicpc.net/problem/11399

from sys import stdin

n = int(stdin.readline())
pi = sorted(list(map(int, stdin.readline().split())))
time = 0
answer = list()
for i in pi:
    time = i+time
    answer.append(time)

print(sum(answer))
