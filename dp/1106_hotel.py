# 숫자를 입력받고 콜라츠 추측 과정을 출력해 주세요.
n = int(input())

while n != 1:
    if n % 2:
        n = n * 3 + 1
        print(n)
    else:
        n //= 2
        print(n)