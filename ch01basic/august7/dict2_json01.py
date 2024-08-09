# PythonDatabaseJsp.pdf  p. 19
person_dict = {
    'age': 20, 'name': '유현식', 'hobby': '독서',
    'address': {'city': 'seoul', 'gu': '마포구', 'zipcode': '12345'}
}
print('person_dict type:', type(person_dict))
print(person_dict)

import json
person_string = json.dumps(person_dict, ensure_ascii=False, indent=4, sort_keys=True)  # 사전을 문자열로 변환

print('person_string type:', type(person_string))
print(person_string)

person_json = json.loads(person_string)
print('person_json type:', type(person_json))
print('이름:', person_json['name'])
print('나이:', person_json['age'])
print('취미:', person_json['hobby'])
print('도시:', person_json['address']['city'])
print('구:', person_json['address']['gu'])
print('우편번호:', person_json['address']['zipcode'])

