# https://www.acmicpc.net/problem/4963

from sys import stdin
read = stdin.readline

from collections import deque

answer = list()

def dfs(mat, vis, start, count):
    stack = deque()
    stack.append(start)

    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    while stack:
        x, y = stack.pop()
        vis[x][y] = count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < len(mat) and -1 < ny < len(mat[0]):
                if vis[nx][ny] == 0 and mat[nx][ny] == 1:
                    vis[nx][ny] = count
                    stack.append((nx, ny))

run = True
while run:
    w, h = map(int, input().split())
    if w is 0 and h is 0:
        run = False
        break

    matrix = [list(map(int, read().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 1

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                dfs(matrix, visited, (i,j), count)
                count += 1

    answer.append(count-1)

print(*answer)
