import sys

n = int(input())
stone = [[0, 0]]

for i in range(n - 1):
    stone.append(list(map(int, sys.stdin.readline().split())))
k = int(input())

dp = [[1e9] * 2 for _ in range(n + 1)]
dp[0][0] = 0
dp[1][0] = 0

if n >= 3:
    dp[2][0] = stone[1][0]
    dp[3][0] = min(dp[2][0] + stone[2][0], dp[1][0] + stone[1][1])
    for i in range(4, n + 1):
        dp[i][0] = min(dp[i - 1][0] + stone[i - 1][0], dp[i - 2][0] + stone[i - 2][1])
        dp[i][1] = min(min(dp[i - 1][1] + stone[i - 1][0], dp[i - 2][1] + stone[i - 2][1]), k + dp[i - 3][0])
elif n == 2:
    dp[2][0] = stone[1][0]

print(min(dp[n][0], dp[n][1]))
