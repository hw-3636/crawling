coffees = dict() # empty dict

coffees['에스프레소'] = 1000
coffees['에스프레소'] = 1500

coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마키야또'] = 4000
print(coffees)

target_item = '카페라떼'
if target_item in coffees:
    print('%s 음료가 있습니다.' % target_item)
else:
    print('%s 음료가 없습니다.' % target_item)

# `핫초코`가 있는지 확인하고, 없으면 5000원으로 추가
target_item = '핫초코'
if not target_item in coffees:
    coffees[target_item] = 5000

print(coffees)

print(coffees.keys())  # 키 값만 출력
print(coffees.values())  # value 값만 출력

# 단가가 6000원 짜리 음료가 있는지 확인하고, 없으면 아이스커피 6000원으로 추가
price = 6000
if not price in coffees.values():
    coffees['아이스커피'] = price

print(coffees)

coffee_list = ['바닐라라떼', '미드나잇베르가못콜드브루', '딸기라떼', '콜드브루']

# 키 값 추출
for key in coffee_list:
    print(key)

# 인덱스 추출
for idx in range(len(coffee_list)):
    print(idx)

# 리스트의 음료를 7000원부터 1000원씩 올려가며 사전에 추가
for idx in range(len(coffee_list)):
    coffees[coffee_list[idx]] = (idx + 7) * 1000

# 리스트 중 dict 에 없는 음료는 5000원으로 추가합니다.
target_list = ['미드나잇베르가못콜드브루', '두유라떼']
for key in target_list:
    try:
        price = coffees[key]
        print('품명: %s, 가격: %d' % (key, price))
    except KeyError:
        print('"%s"가 존재하지 않으므로 항목에 추가합니다.' % key)
        coffees[key] = 5000

# for key in target_list:
#     if not key in coffees:
#         print('"%s"가 존재하지 않으므로 항목에 추가합니다.' % key)
#         coffees[key] = 5000

print(coffees)

target_item = '둥굴레차'
price = coffees.get(target_item, 3000)
print('품명: %s, 가격: %d' % (target_item, price))

# 에스프레소 항목 제거
del coffees['에스프레소']

# key 와 value 를 아래 형식으로 출력
for(key, value) in coffees.items():
    print('%s의 단가는 %d원입니다.' % (key, value))

# 500원 인상: '카페라떼', '카푸치노'
# 1000원 인하: '핫초코'
# 키 값으로 없는 데이터가 입력되었을 시 수정되지 않았음 표기
try:
    coffees['카페라떼'] = coffees['카페라떼'] + 500
    coffees['카푸치노'] = coffees['카푸치노'] + 500
    coffees['핫초코'] = coffees['핫초코'] - 1000
    coffees['라벤더'] = coffees['라벤더'] - 1000
except KeyError:
    print('coffees 목록에 없는 커피명을 입력하였습니다.')


print(coffees)

for key in coffees.keys():
    if key == '카페라떼' or key == '카푸치노':
        coffees[key] += 500
        print('%s의 단가는 %d원입니다.' % (key, coffees[key]))
    elif key == '핫초코':
        coffees[key] -= 1000
        print('%s의 단가는 %d원입니다.' % (key, coffees[key]))
    else:
        print('%s의 단가는 %d원입니다.' % (key, coffees[key]))




print(type(coffees))

coffees.clear()

if len(coffees) == 0:
    print('coffees is empty')
else:
    print('coffees is not empty')

print(coffees)

