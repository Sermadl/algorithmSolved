def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


t = int(input())

for _ in range(t):
    w, e = map(int, input().split())
    bridge = factorial(e)//(factorial(w)*factorial(e-w))
    print(bridge)
