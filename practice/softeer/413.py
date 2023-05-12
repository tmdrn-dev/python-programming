# https://softeer.ai/practice/info.do?idx=1&eid=413

n = int(input())
points = 3
answer = points

for i in range(1, n):
    answer = answer + 2**i

print(answer**2)