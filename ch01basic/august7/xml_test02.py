# PythonDatabaseJsp.pdf  p. 20
# 파이썬 dict(사전) 데이터를 xml 형식으로 변환
from xml.etree.ElementTree import Element, ElementTree, SubElement

my_dict = {
    'hong': ('홍길동', 60, 80, 70),  # tuple
    'park': ('박영희', 50, 70, 95)   # tuple
}

xml_data = Element('students') # 루트 엘리먼트

for key, my_tuple in my_dict.items():
    # print(key)
    # print(my_tuple)
    student = SubElement(xml_data, 'student')  # 서브 엘리먼트
    student.attrib['id'] = key  # key 값으로 서브 엘리먼트 `student` 의 'id=' !!속성!! 추가

    kor = my_tuple[1]
    eng = my_tuple[2]
    math = my_tuple[3]

    total = kor + eng + math
    average = float(total / (len(my_tuple) - 1))

    student.attrib['총점'] = str(total)
    student.attrib['평균'] = '%.3f' % average

    SubElement(student, '이름').text = my_tuple[0]
    SubElement(student, '국어').text = str(my_tuple[1])
    SubElement(student, '영어').text = str(my_tuple[2])
    SubElement(student, '수학').text = str(my_tuple[3])


# 적절하게 들여쓰기 해주는 메서드
def indent(elem, level=0):
    my_tab = '\t'
    i = '\n' + level * my_tab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + my_tab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def

indent(xml_data)

print(type(student))
print(type(xml_data))
xml_file = 'xml_test02.xml'
ElementTree(xml_data).write(xml_file, encoding='UTF-8')
print(xml_file + '파일 생성')


