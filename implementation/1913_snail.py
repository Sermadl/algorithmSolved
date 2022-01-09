n = int(input())
locate = int(input())
snail = [[0] * n for _ in range(n)]
x = n//2
y = n//2
num = 1
snail[x][y] = num
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = 0
cnt = 1
locate_x = 0
locate_y = 0

while num != n*n:
    if direction == 0:
        for j in range(cnt):
            num += 1
            x += dx[direction]
            snail[x][y] = num
            if num == n*n:
                break
        direction += 1
    elif direction == 1:
        for j in range(cnt):
            num += 1
            y += dy[direction]
            snail[x][y] = num
        cnt += 1
        direction += 1
    elif direction == 2:
        for j in range(cnt):
            num += 1
            x += dx[direction]
            snail[x][y] = num
        direction += 1
    elif direction == 3:
        for j in range(cnt):
            num += 1
            y += dy[direction]
            snail[x][y] = num
        cnt += 1
        direction = 0
for i in range(n):
    for j in range(n):
        print(snail[i][j], end = ' ')
        if locate == snail[i][j]:
            locate_x = i
            locate_y = j
    print()
print(locate_x+1, locate_y+1)
