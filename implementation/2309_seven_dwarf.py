import sys

dwarf = []

for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))

dwarf.sort()

for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(dwarf[k])
            exit()