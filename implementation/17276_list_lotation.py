import sys
input = sys.stdin.readline()
t = int(input())

for _ in range(t):

    n, d = map(int, input.split())
    x = []

    for _ in range(n):
        x.append(list(map(int, input.split())))

