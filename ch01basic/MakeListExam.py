# p. 7

# coffees = []  # empty list
coffees = list()

coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인')
coffees.append('카페라떼')

print(coffees)
count = len(coffees)
print('요소 개수: %d개' % count)

# 인덱싱 - 데이터 구조에서 요소를 고유한 위치를 통해 직접 참조하는 기법
print('뒤에서 첫번째 음료: %s' % coffees[-1])
print('앞에서 두번째 음료: %s' % coffees[1])

# 슬라이싱 - 데이터 구조에서 연속적인 요소의 하위 집합을 추출하는 기법
print('0번째부터 3번째 요소까지: %s' % coffees[0:3])
print('4번째 요소부터 마지막 요소까지: %s' % coffees[3:])
print('맨 앞부터 3번째 요소까지: %s' % coffees[:3])

print('# 오름차순 정렬')
coffees.sort()
print(coffees)

print('# 내림차순 정렬')
coffees.sort(reverse=True)
print(coffees)

print('# 요소 순서 랜덤 섞기')
import random
random.shuffle(coffees)
print(coffees)