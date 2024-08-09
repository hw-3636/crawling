coffees = set()  # empty set(집합)

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노')

print(len(coffees))
print(coffees)

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

print(len(coffees))
print(coffees)

newItem = ['콜드브루', '고구마라떼', '디카페인커피']
coffees.update(newItem)

print(len(coffees))
print(coffees)

print('===카푸치노 존재 여부 확인===')
target_item = '카푸치노'
has_item = target_item in coffees
print('%s 존재 여부: %s' % (target_item, has_item))

print('===마키야또 존재 여부 확인 및 추가===')
target_item = '마키야또'
if not target_item in coffees:
    print('%s을(를) 목록에 추가합니다.' % target_item)
    coffees.add(target_item)

print('===믹스커피 존재 여부 확인 및 삭제===')
target_item = '믹스커피'
print('%s을(를) 목록에서 삭제합니다.' % target_item)
coffees.remove(target_item)

print('===바닐라라떼를 목록에서 찾아보고 있으면 삭제, 없으면 존재하지 않음 메시지===')
try:
    target_item = '바닐라라떼'
    coffees.remove(target_item)
except KeyError:
    print('%s은(는) 목록에 존재하지 않습니다.' % target_item)


# 합집합 구하기
coffee01 = set(['고구마라떼', '에스프레소', '아메리카노', '마키야또'])
coffee02 = set(['아메리카노', '마키야또', '카페라떼', '디카페인커피'])

union_set = coffee01.union(coffee02)
print('합집합01: %s' % union_set)

union_set = coffee01 | coffee02
print('합집합02: %s' % union_set)

intersection_set = coffee01.intersection(coffee02)
print('교집합01: %s' % intersection_set)

intersection_set = coffee01 & coffee02
print('교집합02: %s' % intersection_set)

difference_set = coffee01.difference(coffee02)
print('차집합(coffee01-coffee02): %s' % difference_set)
difference_set = coffee01-coffee02
print('차집합(coffee01-coffee02): %s' % difference_set)

difference_set = coffee02.difference(coffee01)
print('차집합(coffee02-coffee01): %s' % difference_set)
difference_set = coffee02-coffee01
print('차집합(coffee02-coffee01): %s' % difference_set)

symmetric_difference_set = coffee01.symmetric_difference(coffee02)
print('차집합들의 합집합: %s' % symmetric_difference_set)

super_set = set(['고구마라떼', '에스프레소', '아메리카노', '마키야또'])
sub_set01 = set(['고구마라떼', '에스프레소'])  # super_set 의 부분 집합
sub_set02 = set(['바닐라라떼', '마키야또'])  # super_set 의 부분 집합 x

issubset_test = sub_set01.issubset(super_set)
if issubset_test:
    print('집합01은 슈퍼 집합의 부분 집합')
else:
    print('집합01은 슈퍼 집합의 부분 집합 아님')

issuperset_test = sub_set02.issuperset(super_set)
if issuperset_test:
    print('super_set 은 집합02의 상위 집합')
else:
    print('super_set 은 집합02의 상위 집합 아님')