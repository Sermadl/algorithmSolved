n, k = map(int, input().split())
length = list(map(int, input().split()))

if k // sum(length) == 0:
    for i in range(n):
        k -= length[i]
        if k < 0:
            print(i+1)
            break
else:
    k %= sum(length)
    for i in range(n-1, -1, -1):
        k -= length[i]
        if k < 0:
            print(i+1)
            break
