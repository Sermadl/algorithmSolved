import sys
input = sys.stdin.readline

n = int(input())
schedule = [0] * 366

for _ in range(n):
    a, b = map(int, input().split())
    #dates = b - a + 1

    for i in range(a, b + 1):
        schedule[i] += 1

row = 0
col = 0
area = 0
for i in range(366):
    if schedule[i] == 0:
        area += row * col
        row = 0
        col = 0
    else:
        col += 1
        row = max(row, schedule[i])
area += row * col
print(area)
