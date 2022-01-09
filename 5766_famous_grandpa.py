import sys


while True:
    rank = {}
    for i in range(1, 10001):
        rank[i] = 0
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break
    else:
        for i in range(n):
            weekly = list(map(int, sys.stdin.readline().split()))
            for j in range(m):
                rank[weekly[j]] += 1
    rank = sorted(rank.items(), key=lambda x: x[1], reverse=True)
    i = 0
    key = []
    for k, v in rank:
        i += 1
        if i == 2:
            key.append(k)
            second = v
        elif i > 2 and v == second:
            key.append(k)

    for i in key:
        print(i, end=' ')
    print()