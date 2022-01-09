import sys


def dfs(node, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in node[v]:
        if visited[i] == 0:
            dfs(node, i, visited)


n = int(input())

node = [[] for _ in range(n+1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

visited = [0] * (n + 1)
dfs(node, 1, visited)
