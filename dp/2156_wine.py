import sys

n = int(input())
wine = []
dp = [0] * n

for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp[0] = wine[0]

if n == 1:
    print(dp[0])
elif n == 2:
    dp[1] = dp[0] + wine[1]
    print(dp[1])
else:
    dp[1] = dp[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i] + wine[i - 1])
    print(dp[n-1])
