'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''

from sys import stdin
read = stdin.readline

for i in range(int(input())):
    N, M = map(int, read().split())
    job = list(map(int, read().split()))

    print(N, M, job)