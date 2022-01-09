word = str(input())

tag = False
start = 0
answer = []
rev = []
for i in range(len(word)):
    if not tag:
        if word[i] == '<':
            if i != 0:
                answer.append(''.join(reversed(rev)))
            rev = ''
            tag = True
            start = i
        elif word[i] == ' ':
            answer.append(''.join(reversed(rev)))
            answer.append(' ')
            rev = ''
        else:
            rev += word[i]
    else:
        if word[i] == '>':
            tag = False
            answer.append(word[start:i+1])

answer.append(''.join(reversed(rev)))

for i in answer:
    print(i, end='')
