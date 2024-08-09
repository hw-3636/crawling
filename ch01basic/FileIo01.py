# p. 17
# 파일에 기록
my_file01 = open('mem.txt', mode='w', encoding='UTF-8')  # 파일 오픈
members = ['홍영식', '김민수', '박진철', '강호숙']

for member in members:
    message = '\'%s\'님 안녕하세요.\n' % member
    my_file01.write(message)

# 기존 파일에 추가
my_file02 = open('mem.txt', mode='a', encoding='UTF-8')

members = ['신유빈', '김진호', '하형주']

for idx in range(len(members)):
    message = '%d번째 고객님: \'%s\'님\n' % (idx+1, members[idx])
    my_file01.write(message)

# 파일 닫기
my_file01.close()

# 'with 구문을 사용하여 close() 함수 사용 없이 파일 닫기
with open('test.txt', mode='w', encoding='UTF-8') as test_file:
    test_file.write("가나다\n")
    test_file.write("abc\n")
    test_file.write("123\n")

    print('hello, world!', file=test_file)

