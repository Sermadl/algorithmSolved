n = int(input())
integer = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if integer[j] < integer[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))