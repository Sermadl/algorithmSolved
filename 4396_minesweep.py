import sys

n = int(input())

mine = []
for i in range(n):
    mine.append(list(map(str, sys.stdin.readline().rstrip())))

visit = []
for i in range(n):
    visit.append(list(map(str, sys.stdin.readline().rstrip())))

dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

def checkbomb(x, y):
    cnt = 0
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            if mine[nx][ny] == '*':
                cnt += 1
    return cnt

check = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 'x':
            if mine[i][j] == '*':
                check = 1
            else:
                visit[i][j] = checkbomb(i, j)

if check == 1:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                visit[i][j] = '*'
for i in visit:
    for j in i:
        print(j, end='')
    print()