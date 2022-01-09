import sys
n = int(input())

result = 0
for _ in range(n):
    words = str(sys.stdin.readline().rstrip())
    di = {}
    isword = True

    for i in range(len(words)):
        if words[i] not in di:
            di[words[i]] = 1
        else:
            if words[i-1] != words[i]:
                isword = False
                break
    if isword:
        result += 1

print(result)
