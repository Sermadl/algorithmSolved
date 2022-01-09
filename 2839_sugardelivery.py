sugar = int(input())

sum = 0
while sugar >= 0:
    if sugar % 5 == 0:
       sum += (sugar // 5)
       print(sum)
       break
    sugar -= 3
    sum += 1
else:
    print(-1)