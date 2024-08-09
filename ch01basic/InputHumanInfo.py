# p.2
print('이름 입력: ', end='')  # end='' print에 엔터가 아닌 띄어쓰기 옵션 주기
name = input()

# input() 함수의 반환 타입: 문자열
age = int(input('나이 입력: '))
height = float(input('키 입력: '))

print('% 포맷 코드로 출력')
print('이름: %s' % name)
print('나이: %d세' % age)
print('키: %.2f' % height)
print('제 이름은 %s 이고, 나이는 %d세 입니다.' % (name, age))
print()


print('문자열 함수 format() 사용')
message = '제 이름은 {} 이고, 나이는 {}세 입니다.\n제 키는 {:.2f}cm 입니다.'
print(message.format(name, age, height))
print()


print('f-string 사용')
print(f'제 이름은 {name} 이고, 나이는 {age}세 입니다.\n제 키는 {height:.2f}cm 입니다.')
