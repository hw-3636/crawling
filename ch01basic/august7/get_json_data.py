# PythonDatabaseJsp.pdf - p. 18
file_name = 'jumsu.json'  # .json 이지만 txt 파일임

my_file = open(file_name, mode='rt', encoding='UTF-8')
my_string = my_file.read()
my_file.close()

import json
json_data = json.loads(my_string)

people = list()  # tuple 데이터의 집합 리스트
for person in json_data:
    name = person['name']
    print('이름:', name)

    kor = float(person['kor'])
    eng = float(person['eng'])
    math = float(person['math'])

    total = kor + eng + math

    _gender = person['gender'].upper()
    if _gender == 'M':
        gender = '남자'
    elif _gender == 'F':
        gender = '여자'
    else:
        gender = '성별 누락'

    message = 'None'
    if 'hello' in person.keys():
        message = person['hello']
        print('메시지:', message)

    my_tuple = (name, kor, eng, math, total, gender, message)
    people.append(my_tuple)


print('json_data type:', type(json_data))
print('my_string type: ', type(my_string))
print('person type: ', type(person))


