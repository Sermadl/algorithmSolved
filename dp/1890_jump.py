n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
result = 0

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        num = game[i][j]

        if j + num < n:
            dp[i][j + num] += dp[i][j]
        if i + num < n:
            dp[i + num][j] += dp[i][j]
