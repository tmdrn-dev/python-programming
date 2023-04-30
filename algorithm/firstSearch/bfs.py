from collections import deque
# stack과 recursion으로 가능
# https://kingpodo.tistory.com/48?category=805745

graph = [
[0,1,1,1,0,0,0], #0
[1,0,0,0,1,0,0], #1
[1,0,0,0,1,1,0], #2
[1,0,0,0,0,1,0], #3
[0,1,1,0,0,0,1], #4
[0,0,1,1,0,0,1], #5
[0,0,0,0,1,1,0]] #6

# 1. 정점 i를 방문
# 2. 정점 i에 인접한 정점 중, 방문하지 않은 정점들을 Queue에 enqueue
# 3. queue에서 pop한 후 해당 node를 기준으로 1부터 반복
# 4. stack이 Null이 되면 종료

visited = list()
queue = deque()

queue.append(0)
while queue:
    node = queue.popleft()
    print("current node: {}".format(node))
    if node not in visited:
        visited.append(node)
    for nextNode in range(len(graph)):
        if (graph[node][nextNode] is 1) and (nextNode not in visited):
            queue.append(nextNode)
    print("stack: {}".format(stack))

print(visited)