import sys
n, m, rotate = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(rotate):
    for i in range(min(n, m) // 2):
        tmp = a[i][i]
        x, y = i, i
        for j in range(i + 1, n - i):
            x = j
            move = a[x][y]
            a[x][y] = tmp
            tmp = move
        for j in range(i + 1, m - i):
            y = j
            move = a[x][y]
            a[x][y] = tmp
            tmp = move
        for j in range(i + 1, n - i):
            x = n - j - 1
            move = a[x][y]
            a[x][y] = tmp
            tmp = move
        for j in range(i + 1, m - i):
            y = m - j - 1
            move = a[x][y]
            a[x][y] = tmp
            tmp = move

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
