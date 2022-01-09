n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

p = [0 for _ in range(n)]
for i in range(k):
    for j in range(n):
        num = s[j]
        index = d[j] - 1

        p[index] = num
    s = list(p)

for i in p:
    print(i, end=' ')
