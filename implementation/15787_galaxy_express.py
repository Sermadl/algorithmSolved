import sys
from collections import deque

cnt_train, cnt_ord = map(int, sys.stdin.readline().split())

order = []
for i in range(cnt_ord):
    order.append(list(map(int, sys.stdin.readline().split())))

trains = [[0] * 20 for _ in range(cnt_train)]

for a in order:
    if a[0] == 1:
        if trains[a[1] - 1][a[2] - 1] == 0:
            trains[a[1] - 1][a[2] - 1] = 1
        else:
            continue
    elif a[0] == 2:
        if trains[a[1] - 1][a[2] - 1] == 1:
            trains[a[1] - 1][a[2] - 1] = 0
        else:
            continue
    elif a[0] == 3:
        i = a[1] - 1
        copy = list(trains[i])

        for j in range(20):
            if j != 19:
                if j == 0:
                    trains[i][j] = 0
                trains[i][j+1] = copy[j]
            else:
                continue
    elif a[0] == 4:
        i = a[1] - 1
        copy = trains[i]

        for j in range(19, -1, -1):
            if j != 0:
                if j == 19:
                    trains[i][j] = 0
                trains[i][j-1] = copy[j]
            else:
                continue

print(len(list(set([tuple(set(train)) for train in trains]))))
