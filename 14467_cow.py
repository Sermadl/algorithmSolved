import sys

observe = int(input())
cow = [-1] * 11
cnt = 0

for _ in range(observe):
    a, b = map(int, sys.stdin.readline().split())
    if cow[a] == -1:
        cow[a] = b
    else:
        if cow[a] != b:
            cnt += 1
            cow[a] = b
print(cnt)