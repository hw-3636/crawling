# p. 6

import random

answer = random.randint(1,100)
print('정답 : %d' % answer)

inputInt = 0
count = 0
while True:  # 무한 while 루프
    inputInt = int(input('1부터 100 사이의 정수 입력 : '))

    count += 1

    if inputInt < 1 or inputInt >100:
        print('%d은(는) 유효하지 않은 정수입니다. 1부터 100 사이의 정수를 입력해 주세요.' % inputInt)
        count -= 1
        continue

    if inputInt > answer:
        print('%d보다 작은 수를 입력해 주세요.' % inputInt)

    elif inputInt < answer:
        print('%d보다 큰 수를 입력해 주세요.' % inputInt)

    else:
        print('정답을 맞추셨습니다!')
        break
    # end if
# end while
print('%d번만에 정답을 맞추셨습니다.' % count)
