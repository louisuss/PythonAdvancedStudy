# yield
# Coroutine

# yield: 메인 루틴 <-> 서브 루틴 간의 통신 가능하게 함
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# 서브루틴: 메인루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스
# 코루틴: 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 다시 원래 위치로 돌아와 수행 가능
# 코루틴: 스케줄링 오베헤드가 매우 적다. 하나의 스레드에서 실행하기 때문
# 스레드 : 싱글스레드 -> 멀티스레드: 복잡, 공유되는 자원에 대한 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

# 코루틴 예제1

# 여러 함수를 비동기 수행. 동시성 프로그래밍 가능
from functools import wraps
from inspect import getgeneratorstate


def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received : {}'.format(i))


# 제너레이터 선언
c1 = coroutine1()
# <generator object coroutine1 at 0x7ff783575270> <class 'generator'>
print(c1, type(c1))

# yield 실행 전까지 실행
next(c1)
# 기본으로 None 전달
# next(c1)

# 값 전송
# c1.send(100)

# 잘못된 사용
c2 = coroutine1()
# TypeError: can't send non-None value to a just-started generator
# 먼저 next 실행해야 함
# c2.send(100)

# 코루틴 예제2
# GEN_CREATED: 처음 대기 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPENDED: yield 대기 상태
# GEN_CLOSED: 실행 완료 상태


def coroutine2(x):
    print('>>> coroutine started: {}'.format(x))
    # x 메인 루틴으로 부터 값을 전송 받음
    # y -> 메인루틴이 코루틴에게 send로 보내줘야 되는 값
    y = yield x
    print('>>> coroutine received: {}'.format(y))
    z = yield x+y
    print('>>> coroutine received: {}'.format(z))


c3 = coroutine2(10)

print(getgeneratorstate(c3))
print(next(c3))
# y 에서 대기 상태
print(getgeneratorstate(c3))
# z 에서 대기 상태
print(c3.send(15))

# >>> coroutine received: 20
# StopIteration
# print(c3.send(20))

# decorator로 코루틴 만들기

# 데코레이터 패턴

# 데코레이터를 통해 next 호출하는 부분을 편하게 수정


def coroutine(func):
    """Decorator run until yield"""
    # 코멘트, 내부 어트리뷰트 등을 모두 가지고 가겠다는 의미
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

# send로 보내는 값을 계속 더함


@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


s = sumer()

print(s.send(100))
print(s.send(100))
print(s.send(100))


# 코루틴 예제3(예외 처리)

class SampleException(Exception):
    """설명에 사용할 예외 유형"""


def coroutine_except():
    print('>>> coroutine started')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing...')
            else:
                print('-> coroutine received: {}'.format(x))
    finally:
        print('-> coroutine ending')


# >>> coroutine started
# None
# -> coroutine received: 10
# None
# -> coroutine received: 10
# None
# -> SampleException handled. Continuing...
# None
# -> coroutine received: 1000
# None
# -> coroutine ending
# None

exe_co = coroutine_except()
print(next(exe_co))
print(exe_co.send(10))
print(exe_co.send(10))
print(exe_co.throw(SampleException))
print(exe_co.send(1000))
print(exe_co.close())  # GEN_CLOSED

# 코루틴 예제4


def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average: {}'.format(avg)


avg2 = averager_re()
next(avg2)
avg2.send(10)
avg2.send(30)
avg2.send(40)

# Average: 26.666666666666668
try:
    avg2.send(None)
# 코루틴에서 리턴으로 반환한 값은 예외처리의 value 값으로 확인 가능
except StopIteration as e:
    print(e.value)

# 코루틴 예제5 (yield from)
# StopIteration 자동 처리) -> 3.7 version < -> await으로 바뀜
# 중첩 코루틴 처리


def gen1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = gen1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# StopIteration
# print(next(t1))

t2 = gen1()
# ['A', 'B', 1, 2, 3]
print(list(t2))

# 중첩된 경우 더 빨리 사용 가능
# yield from 으로 치환 가능


def gen2():
    yield from 'AB'
    yield from range(1, 4)


# A
# B
# 1
# 2
# 3
t3 = gen2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))

t4 = gen2()
# ['A', 'B', 1, 2, 3]
print(list(t4))


def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recv: ', str(x))
    x = yield 100
    print('Recv: ', str(x))

# yield from 으로 코루틴간의 통신을 흐름 제어 가능
# main routine에서 서브 루틴을 관리하는 함수를 만들고
# 여러 만들어진 코루틴을 통한 통신관계 사용 가능


def gen4_main():
    yield from gen3_sub()


t5 = gen4_main()

# Sub coroutine.
# 10
# Recv:  7
# 100
# Recv:  77
# StopIteration
print(next(t5))
print(t5.send(7))
print(t5.send(77))
