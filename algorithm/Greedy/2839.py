# https://www.acmicpc.net/problem/2839

from sys import stdin

n = int(stdin.readline())
answer = -1
bucket_5 = int(n/5)

while bucket_5 >= 0:
    bucket_3, remainder = divmod(n-bucket_5*5, 3)
    if remainder is 0:
        answer = bucket_5 + bucket_3
        break
    else:
        bucket_5 -= 1

print(answer)