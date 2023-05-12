# https://softeer.ai/practice/info.do?idx=1&eid=623

from sys import stdin

m, n, k = map(int, stdin.readline().split())
secret = ''.join(map(str, stdin.readline().split()))
menu = ''.join(map(str, stdin.readline().split()))

if n < m:
    print("normal")
elif menu.find(secret) >= 0:
    print("secret")
else:
    print("normal")
