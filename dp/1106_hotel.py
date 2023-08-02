import sys

c, n = map(int, input().split())

cost = []
client = []

for _ in range(n):
    cst, clnt = map(int, sys.stdin.readline().split())
    cost.append(cst)
    client.append(clnt)

dp = [1e9 for _ in range(c+100)]
dp[0] = 0

for i in range(n):
    for k in range(client[i], c+100):
        dp[k] = min(dp[k - client[i]] + cost[i], dp[k])

print(min(dp[c:]))