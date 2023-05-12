# https://softeer.ai/practice/info.do?idx=1&eid=409

from collections import deque
from sys import stdin

n = int(input())
matrix = [list(int(m) for m in stdin.readline().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

count = 1
answer = list()


def bfs(node, count):
    blocks = 0
    queue = deque()
    queue.append(node)

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()
        if visited[x][y] is False:
            visited[x][y] = True
            matrix[x][y] = count
            blocks += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if -1 < nx < n and -1 < ny < n:
                    if visited[nx][ny] is False and matrix[nx][ny] is not 0:
                        queue.append((nx, ny))

    return blocks


for i in range(n):
    for j in range(n):
        if visited[i][j] is False and matrix[i][j] is not 0:
            answer.append(bfs((i, j), count))
            count += 1

print(count-1)
for block in sorted(answer):
    print(block)
