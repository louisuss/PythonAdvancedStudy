# Asyncio
# 동기 - 기다림
# 비동기 I/O - 기다리지 않고 바로 실행
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업 위임 -> Stop 지점 부터 재실행 원리
# Non-Blocking 비동기 처리 적합

# BlockIO -> Thread 사용
# 스레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결

import timeit
from urllib.request import urlopen
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio


urls = ['http://daum.net', 'https://google.com', 'https://apple.com',
        'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()


async def fetch(url, executor):
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # TypeError: object Response can't be used in 'await' expression
    # request 가 blockio이기 때문
    # 이 부분만 스레딩으로 만들어서 해결
    # aiohttp 사용 가능(Asyncio 적용)

    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)
    return res.read[0:5]

# 여러개 동시에 제너레이터 함수 앞에 async 붙임


async def main():
    # 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)
    # yield from -> await
    # asyncio.ensure_future
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    rst = await asyncio.gather(*futures)

    print()
    print('Result: ', rst)


# 스레드 할 때는 메인 함수 영역을 만들어 줘야됨
# 아니면 진입점이 없으면 에러 발생
if __name__ == '__main__':
    # 루프 생성 (여러 개의 제너레이터 함수로 부터 중앙에서 관리)
    loop = asyncio.get_event_loop()

    # 루프 대기
    loop.run_until_complete(main())

    # 함수 실행
    main()
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Time: ', duration)
