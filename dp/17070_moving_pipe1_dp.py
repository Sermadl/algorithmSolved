import sys

n = int(input())
house = []

for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(2, n):
    if house[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
    for j in range(1, n):
        if house[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        if house[i][j] == 0 and house[i][j-1] == 0 and house[i-1][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
print(sum(dp[i][n-1][n-1] for i in range(3)))