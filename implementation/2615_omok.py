import sys

omok = []
for i in range(19):
    omok.append(list(map(int, sys.stdin.readline().split())))

# 우상, 우, 우하, 하
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

def winner():
    for i in range(19):
        for j in range(19):
            if omok[j][i]:
                for k in range(4):
                    x = j + dx[k]
                    y = i + dy[k]
                    cnt = 1
                    while 0 <= x < 19 and 0 <= y < 19 and omok[j][i] == omok[x][y]:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= x + dx[k] < 19 and 0 <= y + dy[k] < 19 and omok[x][y] == omok[x + dx[k]][y + dy[k]]:
                                break
                            if 0 <= j - dx[k] < 19 and 0 <= i - dy[k] < 19 and omok[x][y] == omok[j - dx[k]][i - dy[k]]:
                                break
                            return omok[j][i], j+1, i+1

                        x += dx[k]
                        y += dy[k]
    return 0, -1, -1


color, x, y = winner()

if color != 0:
    print(color)
    print(x, y)
else:
    print(color)
