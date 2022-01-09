import sys

switch = int(sys.stdin.readline())
onoff = list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())
info = []
for i in range(students):
    info.append(list(map(int, sys.stdin.readline().split())))

def boy(num):
    for i in range(switch):
        if (i+1) % num == 0:
            if onoff[i] == 1:
                onoff[i] = 0
            elif onoff[i] == 0:
                onoff[i] = 1

def girl(num):
    i = 1
    while True:
        if num-i >= 0 and num+i < switch and onoff[num-i] == onoff[num+i]:
                i += 1
        else:
            i -= 1
            break
    for j in range(num-i, num+i+1):
        if onoff[j] == 0:
            onoff[j] = 1
        else:
            onoff[j] = 0

for i, j in info:
    if i == 1:
        boy(j)
    elif i == 2:
        girl(j-1)

for i in range(switch):
    print(onoff[i], end=' ')
    if (i+1) % 20 == 0:
        print()