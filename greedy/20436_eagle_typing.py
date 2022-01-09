qwerty = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
moeum = 'yuiophjklbnm'

l, r = input().split()
letter = list(input())
lx = 0
ly = 0
rx = 0
ry = 0
time = 0
for i in range(len(qwerty)):
    if l in qwerty[i]:
        lx = i
        ly = qwerty[i].index(l)
    if r in qwerty[i]:
        rx = i
        ry = qwerty[i].index(r)

for i in letter:
    if i in moeum:
        for j in range(len(qwerty)):
            if i in qwerty[j]:
                nx = j
                ny = qwerty[j].index(i)

                time += abs(nx - rx) + abs(ny - ry)
                rx = nx
                ry = ny
                break
    else:
        for j in range(len(qwerty)):
            if i in qwerty[j]:
                nx = j
                ny = qwerty[j].index(i)

                time += abs(nx - lx) + abs(ny - ly)
                lx = nx
                ly = ny
                break
    time += 1

print(time)
