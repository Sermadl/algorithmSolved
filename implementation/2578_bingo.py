import sys

bingo = []
mc = []
bingotime = []
for i in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))
for j in range(5):
    mc.append(list(map(int, sys.stdin.readline().split())))


def checkBingo():
    result = 0
    for i in bingo:
        if i.count(0) == 5:
            result += 1

    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt += 1
        if cnt == 5:
            result += 1

    cnt = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt += 1
    if cnt == 5:
        result += 1

    cnt = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        result += 1

    return result


for i in range(5):
    for j in range(5):
        num = mc[i][j]
        for k in range(5):
            for l in range(5):
                if num == bingo[k][l]:
                    bingo[k][l] = 0
        if checkBingo() >= 3:
            bingotime.append(i * 5 + j + 1)
            break
print(min(bingotime))