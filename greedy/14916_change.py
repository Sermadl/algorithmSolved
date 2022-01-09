n = int(input())
result = 0

for i in range(n//5, -1, -1):
    result = i
    change = n - (i * 5)
    if change % 2 == 0:
        result += change // 2
        break
    else:
        result = -1

print(result)
