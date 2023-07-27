n, k = map(int, input().split())
value = []

for j in range(n):
    value.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0
for i in value:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])