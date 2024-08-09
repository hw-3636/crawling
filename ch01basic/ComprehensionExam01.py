my_list01 = [idx for idx in range(1,5)]
print(type(my_list01))
print(my_list01)

my_list02 = [10*i for i in range(1,6)]
print(my_list02)

my_list03 = [i for i in range(1, 101, 3)]
print(my_list03)

my_list04 = [i for i in range(1, 101, 3) if i % 10 == 0]
print(my_list04)

some_data=[75, 30, 85, 50]
my_list05 = [score for score in some_data if score >= 60]
print(my_list05)

# 중첩 for
my_list06 = [x*y for x in range(2, 10) for y in range(1, 10)]
print(my_list06)

# Tuple 을 담고 있는 리스트
fruits = [('바나나', 10), ('사과', 20), ('오렌지', 30)]

for item in fruits:  # 아이템은 Tuple
    print(item[0])
    print(item[1])

my_dict01 = {item[0] : item[1] for item in fruits}
print(my_dict01)

students = [  # 학생들의 시험 점수를 사전으로 만들어 보세요.
    ('이문식', 80, 90, 50),
    ('강수현', 50, 60, 80),
    ('윤정혁', 70, 40, 60)
]

# 학생의 첫번째 점수
my_dict02 = {item[0] : item[1] for item in students}
print(my_dict02)

# 학생별 점수 합계
my_dict03 = {item[0]:sum(item[1:]) for item in students}
print(my_dict03)

