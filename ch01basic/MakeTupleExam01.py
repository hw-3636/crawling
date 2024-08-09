coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')

# 요소들을 콤마로 연결하면 tuple 으로 인식 1
coffee03 = '카푸치노', '마키야또'

my_tuple = coffee01 * 3
print(my_tuple)

my_list = ['바닐라라떼', '플랫화이트']
coffee04 = tuple(my_list)  # 리스트를 튜플로 변환
print(type(coffee04))

# TypeError: can only concatenate tuple (not "str") to tuple
# coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소')

# 요소들을 콤마로 연결하면 tuple 으로 인식 2
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
print(type(coffees))

length = len(coffees)
print('요소 개수: %d' % length)
print(coffees)

# 불변성을 가지는 tuple, 값을 할당할 수 없다.
# coffees[1] = '우유'

# 인덱싱과 슬라이싱
print('앞에서 3번째 요소: %s' % coffees[2])
print('뒤에서 2번째 요소: %s' % coffees[-2])

print('첫번째부터 세 번째 까지의 요소', end='')
print(coffees[:3])
print('네번째 이후의 모든 요소', end='')
print(coffees[3:])

my_count = coffees.count('아메리카노')
print(my_count)
my_index = coffees.index('콜드브루')
print(my_index)


