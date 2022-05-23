import sys

n = int(input())
order = []
result = 0

for _ in range(n):
    order.append(int(sys.stdin.readline()))

order.sort(reverse=True)

for i in range(n):
    if order[i]-i < 0:
        continue
    result += order[i]-i

print(result)