import sys

A = []

for i in range(9):
    A.append(int(sys.stdin.readline()))
s = sum(A)
A.sort()
for i in range(9):
    for j in range(i+1, 9):
        if s - A[i] - A[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(A[k])
