import sys


def dfs(graph, v):
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(graph, i)


computer = int(input())
n = int(input())

graph = [[] for _ in range(computer+1)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
dfs(graph, 1)
print(len(visited)-1)
