import requests
from pprint import pprint #가독성 좋게 출력하기 위해 사용하는 모듈
json_url = "https://raw.githubusercontent.com/pyhub-kr/dump-data/main/melon/melon-20230906.json" 

response = requests.get(json_url)
response.raise_for_status() # 비정상적인 응답을 받았다면, HTTPError 발생시키도록 함

song_list = response.json()

print(type(song_list) , len(song_list) , type(song_list[0])) #테스트 출력
pprint(song_list)