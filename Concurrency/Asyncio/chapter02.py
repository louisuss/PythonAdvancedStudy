# Asyncio
# 동기 - 기다림
# 비동기 I/O - 기다리지 않고 바로 실행
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업 위임 -> Stop 지점 부터 재실행 원리
# Non-Blocking 비동기 처리 적합

# BlockIO -> Thread 사용
# 스레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결

import timeit
# from urllib.request import urlopen
import requests
from concurrent.futures import ThreadPoolExecutor
import threading


urls = ['http://daum.net', 'https://google.com', 'https://apple.com',
        'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()


def fetch(url):
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    requests.get(url)
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)


def main():
    # max_worker=10 넣으면 에러
    with ThreadPoolExecutor() as executor:
        for url in urls:
            # map으로 할 경우 순서대로 하지만 for 문에서 사용불가
            # 따로 매핑해줘야됨
            executor.submit(fetch, url)


# 스레드 할 때는 메인 함수 영역을 만들어 줘야됨
# 아니면 진입점이 없으면 에러 발생
if __name__ == '__main__':
    main()
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Time: ', duration)
