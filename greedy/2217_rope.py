import sys

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline()))
ropes.sort()

weight = []

for i in range(n):
    weight.append(ropes[i] * (n-i))

print(max(weight))