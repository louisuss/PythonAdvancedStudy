# Asyncio
# 동기 - 기다림
# 비동기 I/O - 기다리지 않고 바로 실행
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업 위임 -> Stop 지점 부터 재실행 원리
# Non-Blocking 비동기 처리 적합

# BlockIO

import timeit
# from urllib.request import urlopen
import requests


urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print('Start ', url)
    # 실제 요청
    # 요청하면 응답이 올 때 까지, 즉 urlopen 함수 끝날 때까지 아래부분이 실행 안됨
    text = requests.get(url)
    # text = urlopen(url)
    # 실제 내용
    print('Contents', text)
    print('Done ', url)

# 완료시간 - 시작시간
duration = timeit.default_timer() - start

# 총 실행 시간
print('Total Time: ', duration)