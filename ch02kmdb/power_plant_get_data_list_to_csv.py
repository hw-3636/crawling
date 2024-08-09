import urllib.request
import urllib.parse
import json, math

service_key = '5OIBiXx9qi1pSZaYyUCsS8lRFlLS26M2KE2KCy3a0NOAqbtB1o2TQNa3xKRApw%2Bslk9ygdzrfKTPyOYyo38SGg%3D%3D'

def get_data_from_wep(url):

    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('UTF-8')

    except Exception as e:
        print('크롤링 실패', e, '확인 요망')
        return None

def data_extractor(page_no, num_of_rows):
    end_point = 'http://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getIncoStat_V2'
    parameter = '?serviceKey=' + service_key
    parameter += '&numOfRows=' + str(num_of_rows)
    parameter += '&pageNo=' + str(page_no)
    parameter += '&resultType=json'
    parameter += '&bizYear=2020'

    url = end_point + parameter
    print(url)

    json_data = get_data_from_wep(url)
    print(json_data)

    if json_data == None:
        return None
    else:
        try:
            return json.loads(json_data)
        except Exception as e:
            print('JSON 데이터에 문제가 있습니다.')
            print(e)
            return None


data_extractor(1, 1000)