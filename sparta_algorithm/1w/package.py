from pprint import pprint
import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

pprint(rjson)

rows = rjson['RealtimeCityAir']['row']

for row in rows :
    gu_name = row['MSRSTE_NM']
    gu_mise = row['IDEX_MVL']
    if gu_mise <60 :
        print(gu_name, gu_mise)
        
def get_gu_mise(gu_name) :
    for search in rows :
        if search['MSRSTE_NM'] == gu_name :
            return search['IDEX_MVL']
    return 'nothing'

print(get_gu_mise('중구'))
