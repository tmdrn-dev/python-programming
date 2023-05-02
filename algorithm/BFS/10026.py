# https://www.acmicpc.net/problem/10026

from sys import stdin
read = stdin.readline

size = int(input())
RGB = [list(read().strip()) for _ in range(size)]

from collections import deque
visited = [[0] * size for _ in range(size)]

def bfs(matrix, visited, start, count):
    queue = deque()
    queue.append(start)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < size and -1 < ny < size:
                if visited[nx][ny] == 0 and matrix[x][y] == matrix[nx][ny]:
                    visited[nx][ny] = count
                    queue.append((nx, ny))
count = 1
for i in range(size):
    for j in range(size):
        if visited[i][j] is 0:
            bfs(RGB, visited, (i,j), count)
            count += 1

answer = list()
answer.append(count-1)

visited = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if RGB[i][j] is 'G':
            RGB[i][j] = 'R'

count = 1
for i in range(size):
    for j in range(size):
        if visited[i][j] is 0:
            bfs(RGB, visited, (i,j), count)
            count += 1

answer.append(count-1)
print(*answer)