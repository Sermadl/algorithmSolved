n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
oil = price[0]
result = 0

for i in range(n-1):
    if oil > price[i]:
        oil = price[i]
    result += (distance[i] * oil)

print(result)