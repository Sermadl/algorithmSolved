n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
    sum = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(sum)
print(fibonacci[n])
