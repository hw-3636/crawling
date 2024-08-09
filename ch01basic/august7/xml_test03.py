# PythonDatabaseJsp.pdf  p. 21

from xml.etree.ElementTree import parse

tree = parse(source='car_info.xml')

my_root = tree.getroot()  # tree xml 데이터(car_info.xml)를 파이썬의 Element 클래스 타입으로 전부 가져오기
print('my_root type', type(my_root))

cars = my_root.findall('car')
print('cars type', type(cars))
print('총 car 수:', len(cars))
print('-'*30)

for car in cars:
    print('car 구성 정보')
    brand = car[0].text
    brand_name = car[0].attrib['name']
    model = car[1].text
    release_year = car[2].text
    color = car[3].text.upper()

    print('브랜드(한글 이름):', brand)
    print('브랜드(영어 이름):', brand_name)
    print('모델명:', model)
    print('출시 년도: %s년' % release_year)
    print('색상:', color)
    print('-'*30)




