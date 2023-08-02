import sys

n = int(input())
profit = []

for _ in range(n):
    profit.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (n+1)

m = 0

for i in range(n):
    m = max(m, dp[i])
    if i + profit[i][0] <= n:
        dp[i + profit[i][0]] = max(m + profit[i][1], dp[i + profit[i][0]])

print(max(dp))
