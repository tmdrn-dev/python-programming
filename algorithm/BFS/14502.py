# https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque
from itertools import combinations

answer = 0
n, m = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

viruses = list()
empty = list()
for i in range(n):
    for j in range(m):
        if matrix[i][j] is 2:
            viruses.append((i,j))
        elif matrix[i][j] is 0:
            empty.append((i,j))

walls = combinations(empty, 3)
_matrix = list([0]*m for _ in range(n))

for wall in walls:
    # Deep copy original matrix
    for i in range(n):
        for j in range(m):
            _matrix[i][j] = matrix[i][j]

    # Install walls to copied matrix
    for i, j in wall:
        _matrix[i][j] = 1

    # Start BFS from virus
    for virus in viruses:
        queue = deque()
        queue.append(virus)
        
        di = [0, -1, 0 , 1]
        dj = [1, 0, -1 , 0]

        while queue:
            i, j = queue.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if -1 < ni < n and -1 < nj < m:
                    if _matrix[ni][nj] == 0:
                        _matrix[ni][nj] = 2
                        queue.append((ni, nj))

    # Count safety zone
    safety = 0
    for row in _matrix:
        safety += row.count(0)

    # Update the biggest safety zone
    answer = max(answer, safety)

print(answer)
