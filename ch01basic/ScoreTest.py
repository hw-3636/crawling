def score_info(name, kor, eng=50, math=60):  # eng 의 기본 값은 50, math 의 기본 값은 60
    total = kor + eng + math
    average = total / 3.0

    if average >= 70.0:
        pass_or_fail = '합격'
    else:
        pass_or_fail = '불합격'
    print('%s 학생의 정보')
    print('국어: %d, 영어: %d, 수학: %d' % (kor, eng, math))
    print('총점: %d, 평균: %.2f, 합격 여부: %s' % (total, average, pass_or_fail))


name, kor, eng, math = '김철수', 50, 60, 70
score_info(name, kor, eng, math)  # positional argument
score_info('박영희', 80)  # positional argument
score_info(math=30, eng=90, name='심현철', kor=100)  # keyword argument
score_info('권유정', 50, math=70)  # 혼합 형태 - positional 먼저 온 이후 keyword 나열

