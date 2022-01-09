n = int(input())

star = []
line = (n-1)*4+1
star.append('*'*line)
if n != 1:
    for i in range((n-1)*2):
        if i % 2 == 0:
            a = (n-2)*4+1-(i*2)
            b = (i//2+1)
            star.append('* '*b + ' '*a + ' *'*b)
        else:
            star.append('* '*b + '*'*a + ' *'*b)
for i in star:
    print(i)
for i in range(len(star)-2, -1, -1):
    print(star[i])
