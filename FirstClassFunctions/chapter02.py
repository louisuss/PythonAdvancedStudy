# 파이썬 변수 범위(global)

# b가 없어서 에러
# def func_v1(a):
#     print(a)
#     print(b)


import time
b = 10


def func_v2(a):
    print(a)
    print(b)


func_v2(5)


# 같은 변수가 있을 시 지역 변수가 우선
# def func_v3(a):
#     print(a)
#     print(b)
#     # b가 내 지역안에 있는 것만 확인 가능하고 값은 이후에 대입됨
#     # 에러
#     b = 5
# func_v3(5)

# 클로저
# 반환되는 내부 함수에 대해서 선언 된 연결정보를 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능

a = 10

# 결과 누적 할 수 있을까?

# 더할 때 마다 누적되는 객체 생성


class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


avg_cls = Averager()

# 누적 확인
print(avg_cls(10))
print(avg_cls(35))

# 클로저 사용
# 일반적으로 두개 이상의 함수로 구성
# 전역변수 사용 감소
# 디자인 패턴 적용
# 많이쓰면 자원을 너무 많이 사용


def closure_avg1():
    series = []
    # 외부함수와 내부함수의 사이
    # Free variable
    # 클로저 영역
    # series가 밖에 있음에도 계속 누적되서 사용됨

    def averager(v):
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager


avg_closure1 = closure_avg1()

# 계속 누적됨
print(avg_closure1)
print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(45))

# print(dir(avg_closure1))
# print(dir(avg_closure1.__code__))
# ('series',)
print(avg_closure1.__code__.co_freevars)
# print(dir(avg_closure1.__closure__[0]))
# print(dir(avg_closure1.__closure__[0].cell_contents))


# 잘못된 클로저 사용
def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # 클로저 영역

    def averager(v):
        # 없으면 에러 발생
        nonlocal cnt, total
        cnt += 1
        total += v
        print('def2 >>> {} / {}'.format(total, cnt))
        return total / cnt
    return averager


avg_closure2 = closure_avg2()

# 내부 cnt, total 외부 cnt, total 별개임
# 때문에 nonlocal 예약어 사용
print(avg_closure2(15))
print(avg_closure2(35))
print(avg_closure2(45))


# 데코레이터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함

# 함수 실행 시간 측정

# 클로저 패턴과 일치

def perf_clock(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result: [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)


# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

# <function perf_clock. < locals > .perf_clocked at 0x7fb99be5fb80 > ('func',)
# <function perf_clock. < locals > .perf_clocked at 0x7fb99be5fc10 > ('func',)
# <function perf_clock. < locals > .perf_clocked at 0x7fb99be5fca0 > ('func',)
print(non_deco1, non_deco1.__code__.co_freevars)
print(non_deco2, non_deco2.__code__.co_freevars)
print(non_deco3, non_deco3.__code__.co_freevars)

# **************************************** Called Non Deco -> time_func
# Result: [2.00460s] time_func(2) -> None
print('*'*40, 'Called Non Deco -> time_func')
non_deco1(2)

# **************************************** Called Non Deco -> sum_func
# Result: [0.00000s] sum_func(10, 20, 30) -> 60
print('*'*40, 'Called Non Deco -> sum_func')
non_deco2(10, 20, 30)

# **************************************** Called Non Deco -> fact_func
# Result: [0.00001s] fact_func(10) -> 3628800
print('*'*40, 'Called Non Deco -> fact_func')
non_deco3(10)

# 데코레이터 사용
print('*'*40, 'Called Non Deco -> time_func')
time_func(2)

print('*'*40, 'Called Non Deco -> sum_func')
sum_func(10, 20, 30)

print('*'*40, 'Called Non Deco -> fact_func')
fact_func(10)
