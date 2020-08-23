# 일급 함수 (일급 객체)
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과로 반환 가능 return funcs

# 함수 객체 예제

import random
from operator import add
from functools import reduce


def factorial(n):
    """Factorial Function -> n: int"""
    if n == 1:
        return 1
    return n * factorial(n-1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
# print(dir(factorial))
# print(dir(A))
# 함수만 가지고 있는 특성
print(sorted(set(dir(factorial)) - set(dir(A))))
# 함수명
print(factorial.__name__)
# 작업하는 파일 위치
print(factorial.__code__)

var_func = factorial

print(var_func(5))
# [1, 2, 6, 24, 120]
# map: 함수 인자를 받아 이터레이터 만큼 실행
print(list(map(var_func, range(1, 6))))


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)
# [1, 6, 120]
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

# reduce()
# 함수를 인자로 받는데 이전의 결과값을 reduce 함수로 감소 시키며 add 함수로 더해줌
# 만든 함수에 limit을 주고 계속 줄여가며 합산하거나 결과의 결과를 반환해서 연쇄적으로 사용할 경우 사용
print(reduce(add, range(1, 11)))  # 누적
print(sum(range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x+t, range(1, 11)))

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인

# 로또 추첨 클래스 선언


class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    # 객체를 함수처럼 동작하게 만들 수 있음
    def __call__(self):
        return self.pick()


game = LottoGame()
print(game.pick())

# 호출 가능 확인
# callable로 체크하고자 하는 값을 넣어주면 호출 가능여부 출력
print(callable(str), callable(list), callable(
    factorial), callable(3.14), callable(game))
print(game())

# 파이썬 클래스 -> 함수, 변수, 클래스 자체로 활용 가능

# 다양한 매개변수 입력(*args, **kwargs)
# * - tuple 형 / ** - 딕셔너리 형


def args_test(name, *contents, point=None, **attrs):
    return '<args_test> -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)


# <args_test> -> (test1) (()) (None) ({})
print(args_test('test1'))

# <args_test> -> (test1) (('test2',)) (None) ({})
print(args_test('test1', 'test2'))

# <args_test> -> (test1) (('test2', 'test3')) (None) ({'id': 'admin'})
print(args_test('test1', 'test2', 'test3', id='admin'))

# <args_test> -> (test1) (('test2', 'test3')) (7) ({'id': 'admin'})
print(args_test('test1', 'test2', 'test3', id='admin', point=7))

# <args_test> -> (test1) (('test2', 'test3')) (7) ({'id': 'admin', 'password': '1234'})
print(args_test('test1', 'test2', 'test3', id='admin', point=7, password='1234'))


# 함수 Signatures
# 함수에 인자에 대한 정보를 표시해 줄 수 있는 형태의 메소드
from inspect import signature

sg = signature(args_test)
# (name, *contents, point=None, **attrs)
print(sg)

# OrderedDict([('name', <Parameter "name">), ('contents', <Parameter "*contents">), ('point', <Parameter "point=None">), ('attrs', <Parameter "**attrs">)])
print(sg.parameters)

# 모든 정보 출력
# name POSITIONAL_OR_KEYWORD < class 'inspect._empty' >
# contents VAR_POSITIONAL < class 'inspect._empty' >
# point KEYWORD_ONLY None
# attrs VAR_KEYWORD < class 'inspect._empty' >
for name, param in sg.parameters.items():
    print(name, param.kind, param.default)

# partial 사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용
# 함수의 새 객체 타입은 이전 함수의 자체를 기술하고 있다
from operator import mul
from functools import partial

# 함수를 인수로 받는 경우에 활용 가능
print(mul(10, 100))

# 인수 고정
five = partial(mul, 5)
print(five(100))
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1,11))))

# 고정 추가
six = partial(five, 6)
# 5 고정에 6을 했으므로 인수 꽉참
print(six())


