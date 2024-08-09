# PythonDatabaseJsp.pdf  p. 29 ~
import urllib.request
import urllib.parse
import json, math

# 크롤링 할 사이트에서 오픈 API 서비스 사용을 목적으로 발급 받은 키
service_key = '65dcb126787360405e913f1ffb27f09f'

def get_data_from_web(url):

    req = urllib.request.Request(url)  # (요청 객체) url 정보를 이용해 해당 웹 사이트에서 json 데이터를 읽어와 Request 클래스 타입으로 반환하는 메서드
    try:
        response = urllib.request.urlopen(req)  # (응답 객체)
        # http 응답 성공 시 200(404페이지 같은 느낌~) 반환
        if response.getcode() == 200:
            return response.read().decode('UTF-8')  # 바이트 타입을 문자열로 변환하여 반환

    except Exception as e:
        print('크롤링 실패', e, '확인 요망')
        return None


def movie_extractor(page_number, page_size, year):
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'

    parameter = '?key=' + service_key
    parameter += '&curPage=' + str(page_number)
    parameter += '&itemPerPage=' + str(page_size)
    parameter += '&openStartDt=' + str(year)

    # parameter += '&movieNm=' + '행복의 나라'
    # movie_name = '행복의 나라'
    # encoded_movie_name = urllib.parse.quote(movie_name, encoding='UTF-8')
    # parameter += '&movieNm=' + encoded_movie_name


    url = end_point + parameter
    print(url)

    json_data = get_data_from_web(url)

    if json_data == None:
        return None
    else:
        try:
            return json.loads(json_data)
        except Exception as e:
            print('JSON 데이터에 문제가 있습니다.')
            print(e)
            return None


import pandas as pd

# 영화 정보를 저장할 데이터 프레임
movie_table = pd.DataFrame()  # 판다즈에서 제공하는 데이터 프레임 정의

def make_movie_table(dict_data):
    for movie in movie_data['movieListResult']['movieList']:
        # print(movie['movieCd'])  # 영화 코드
        movie_dict = {
            'movieCd': movie['movieCd'],
            'movieNm': movie['movieNm'],
            'movieNmEn': movie['movieNmEn'],
            'prdtYear': movie['prdtYear'],
            'openDt': movie['openDt'],
            'typeNm': movie['typeNm'],
            'prdtStatNm': movie['prdtStatNm'],
            'nationAlt': movie['nationAlt'],
            'genreAlt': movie['genreAlt'],
            'repNationNm': movie['repNationNm'],
            'repGenreNm': movie['repGenreNm'],
        }
        frame = pd.DataFrame(movie_dict, index=[0])
        # print(frame)

        global movie_table  # movie_table 이 '전역 변수'라고 알리기 위하여 global 키워드 사용
        movie_table = pd.concat([movie_table, frame])

    print('-' * 30)


print('크롤링 중입니다. 잠시만 기다려 주세요.')

start_year, end_year = 2024, 2025
page_size = 100  # 해당 url에 해당하는 페이지는 최대 100개까지 허용해놨기 때문에 100으로 지정

for year in range(start_year, end_year):
    print('%s년도를 크롤링 중입니다.' % year)
    page_number = 1

    while True:
        movie_data = movie_extractor(page_number, page_size, year)

        try:
            totCnt = movie_data['movieListResult']['totCnt']
        except Exception as e:
            # 이번 페이지에 존재하지 않으면 다음 페이지로 넘어가기
            page_number +1
            continue

        if page_number == 1:  # 1페이지일 때만 전체 개수 출력
            print('데이터 총 개수:', str(totCnt))

        if totCnt == 0:  # 총 개수(totCnt)가 0이면 더이상 존재하지 않는 것으로 간주
            break

        total_page = math.ceil(totCnt / page_size)
        print('진행 중인 페이지:', str(page_number), '/', str(total_page))
        make_movie_table(movie_data)

        if page_number == total_page:  # 마지막 페이지에 도달하면 끝내기
        # if page_number == 3:
            break

        page_number += 1  # 다음 페이지로 이동


print('[크롤링이 끝났습니다]')
print(movie_table)
print('movie_table type:', type(movie_table))
print(movie_table.info())

# csv(comma separate value): 텍스트 형식의 파일, 엑셀에서 열 수 있음
file_name = 'kmdb_get_mobie_list.csv'
movie_table.to_csv(file_name, index=False, encoding='UTF-8')
print(file_name + '파일이 저장되었습니다')