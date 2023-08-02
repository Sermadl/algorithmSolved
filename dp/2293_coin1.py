import sys

n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for value in coin:
    for j in range(value, k+1):
        if j - value >= 0:
            dp[j] += dp[j - value]

print(dp[k])