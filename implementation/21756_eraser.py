n = int(input())

erase = []
for i in range(n):
    erase.append(i+1)


while erase:
    A = []
    n //= 2
    for i in range(n):
        A.append(erase[i*2+1])
    if n == 0:
        break
    erase = list(A)

print(erase[0])
