n = int(input())
c = {}

for i in range(n):
    a, b = map(int, input().split())
    c[a] = b

while c:
    