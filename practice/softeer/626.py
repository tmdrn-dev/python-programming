# https://softeer.ai/practice/info.do?idx=1&eid=626

from sys import stdin

n, m = map(int, stdin.readline().split())
rooms = dict()
for _ in range(n):
    room = input()
    rooms[room] = [True]*9

for _ in range(m):
    room, s, t = stdin.readline().split()
    for i in range(int(s)-9, int(t)-9):
        rooms[room][i] = False

count = 1
for room in sorted(rooms):
    answer = list()
    s = -1
    for time, available in enumerate(rooms[room]):
        if available is True:
            if s is -1:
                s = time
            if time == 8:
                answer.append((s+9, time+9+1))
        else:
            if s != -1:
                answer.append((s+9, time+9))
                s = -1

    print("Room {}:".format(room))
    available = len(answer)
    if available:
        print("{} available:".format(available))
    else:
        print("Not available")
    for s, t in answer:
        print("{}-{}".format(str(s).rjust(2, '0'), t))
    if count < len(rooms):
        print("-----")
    count += 1
