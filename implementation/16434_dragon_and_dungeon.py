import math
import sys

n, Hatk = map(int, input().split())

dungeon = []

for _ in range(n):
    dungeon.append(list(map(int, sys.stdin.readline().split())))

Hp = 0
maxHp = 0

for t, a, h in dungeon:
    if t == 1:
        Hp += (math.ceil(h/Hatk) - 1) * a
    else:
        maxHp = max(maxHp, Hp) # Hp의 값이 0으로 바뀔 수도 있으니 maxHp에 저장함
        Hatk += a
        Hp -= h
        if Hp < 0:
            Hp = 0

print(max(maxHp, Hp) + 1)
