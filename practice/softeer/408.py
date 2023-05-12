# https://softeer.ai/practice/info.do?idx=1&eid=408

from sys import stdin
arr = list(map(int, stdin.readline().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = sorted(ascending, reverse=True)

if arr == ascending:
    print("ascending")
elif arr == descending:
    print("descending")
else:
    print("mixed")
