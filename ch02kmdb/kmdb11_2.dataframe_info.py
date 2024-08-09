import pandas as pd
my_coding = 'UTF-8'
file_name = './../data/kmdb_get_movie_list_100.csv'
data_frame = pd.read_csv(file_name, encoding=my_coding)
# print(data_frame.info())

print('행 색인 정보 확인')
print(data_frame.columns)

print('열 색인 정보 확인')
print(data_frame.dtypes)

# print('컬럼별 데이터 유형 확인')
# print(data_frame.dtypes)

# for column in data_frame.columns:
    # print(column)
    # print(data_frame[column].unique())
    # print('-'*30)

# print(sorted(data_frame['movieCd'].unique()))

print('코드 전체가 숫자 형식인 데이터만 필터링')
print('before count: ' + str(len(data_frame)))
data_frame = data_frame[data_frame['movieCd'].str.isdigit()]
print('after count: ' + str(len(data_frame)))

# 'movieCd' 열을 숫자형 형식으로 변환
data_frame['movieCd'] = pd.to_numeric(data_frame['movieCd'])

print(data_frame['repGenreNm'].unique())

print('컬럼별 데이터 유형 확인')
print(data_frame.dtypes)

prdt_year = data_frame['prdtYear']
print(type(prdt_year))

print('시리즈 요소 개수 확인 : ' + str(prdt_year.size))
print('형상 확인 : ' + str(prdt_year.shape))
print('len(prdt_year) : ' + str(len(prdt_year)))
print('count() : ' + str(prdt_year.count))
print('타입 확인 : ' + str(prdt_year.dtype))
print('누락 데이터 여부 : ' + str(prdt_year.hasnans))  # True 일 시 누락 데이터 '있음'
print('모든 항목이 유니크한가? : ' + str(prdt_year.is_unique))  # True 일 시 모든 항목 유니크

print(prdt_year.value_counts())  # 유니크한 항목이 몇개나 있는가


file_name = './../data/kmdb_get_movie_list_100_new.csv'
data_frame.to_csv(file_name, index=False, encoding='UTF-8')
print(file_name + '파일 저장')


