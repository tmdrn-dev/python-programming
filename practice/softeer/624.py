# https://softeer.ai/practice/info.do?idx=1&eid=624

from sys import stdin

numbers = {
    '-': [0,0,0,0,0,0,0],
    '0': [1,1,1,0,1,1,1],
    '1': [0,0,1,0,0,1,0],
    '2': [1,0,1,1,1,0,1],
    '3': [1,0,1,1,0,1,1],
    '4': [0,1,1,1,0,1,0],
    '5': [1,1,0,1,0,1,1],
    '6': [1,1,0,1,1,1,1],
    '7': [1,1,1,0,0,1,0],
    '8': [1,1,1,1,1,1,1],
    '9': [1,1,1,1,0,1,1]
}

n = int(input())
for _ in range(n):
    A, B = input().split()
    for i in range(5-len(A)):
        A = '-' + A
    for i in range(5-len(B)):
        B = '-' + B

    answer = 0
    for i in range(5):
        n = numbers[A[i]]
        m = numbers[B[i]]

        for j in range(7):
            if n[j] != m[j]:
                answer += 1

    print(answer)
