import sys


def dfs(x, y, move):
    answer[x][y] += 1

    if move == 1:
        if y == n - 1:
            return

        if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
            dfs(x, y + 1, 1)

        if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 3)

    elif move == 2:
        if x == n - 1:
            return

        if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
            dfs(x + 1, y, 2)

        if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 3)

    elif move == 3:
        if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
            dfs(x, y + 1, 1)

        if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
            dfs(x + 1, y, 2)

        if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 3)
    return


n = int(input())

house = []
answer = [[0] * n for _ in range(n)]

for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

dfs(0, 1, 1)
print(answer[n - 1][n - 1])
