# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args
# 공부할 것: 반복형 객체 내부적으로 iter 함수 내용, 제너레이터 동작 원리, yield from

# 반복 가능 이유? -> iter(x) 함수 호출

import itertools
from collections import abc
t = 'ABCDEF'

# for
for c in t:
    print(c)
print()

w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration as log:
        print(log)
        break


# 반복형 확인
# True / False return

print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))
print(hasattr(w, '__iter__'))
print(isinstance(w, abc.Iterable))
print()

# next 사용


class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop! Stop!')
        self._idx += 1
        return word

    def __iter__(self):
        print("Called __iter__")
        return self

    # print 문으로 객체 인스턴스 확인 가능
    # 없으면 <__main__.WordSplitIter object at 0x7faf17169730> 처럼 출력
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


w1 = WordSplitIter('Who says the nights are for sleeping.')
# WordSplit(['Who', 'says', 'the', 'nights', 'are', 'for', 'sleeping.'])
print(w1)
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))


# Gererator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제너레이터로 완화
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    # 위의 기능과 동일

    def __iter__(self):
        for word in self._text:
            yield word  # 제너레이터
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


w2 = WordSplitGenerator('Who says the nights are for sleeping.')
w3 = iter(w2)

# <generator object WordSplitGenerator.__iter__ at 0x7fa7fda746d0 >
# Who
# says
# the
# nights
# are
# for
# sleeping.
print(w3)
print(next(w3))
print(next(w3))
print(next(w3))
print(next(w3))
print(next(w3))
print(next(w3))
print(next(w3))
print()

# Generator 예제


def generator_ex1():
    print('start')
    # 이 구문 만나면 다음 next 만날 때 까지 멈춤
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')


temp = iter(generator_ex1())

print(next(temp))
print(next(temp))
print()
# print(next(temp))

for v in generator_ex1():
    print(v)
print()

temp2 = [x*3 for x in generator_ex1()]
temp3 = (x*3 for x in generator_ex1())

# ['AAAAAAAAA', 'BBBBBBBBB']
# 메모리에 만들어서 올림
print(temp2)
# <generator object <genexpr> at 0x7fc862a6a6d0>
# generator로 호출
# next 메소드 호출 전까지 만들지 않음
print(temp3)

# 출력
for i in temp3:
    print(i)
print()

# Generator 자주 사용하는 함수

# 1
# 3.5
# 6.0
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))

# takewhile로 조건 지정
gen2 = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2.5))

for v in gen2:
    print(v)

# 필터 반대 (조건과 반대인 값들 출력)
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

# 누적 합계
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
gen4 = itertools.accumulate([x for x in range(1, 10)])

for v in gen4:
    print(v)

# 연결1
# ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

# 연결2
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# 개별로 쪼개줌
# [('A',), ('B',), ('C',), ('D',), ('E',)]

gen7 = itertools.product('ABCDE')
print(list(gen7))

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
gen8 = itertools.product('ABC', repeat=2)
print(list(gen8))

# 그룹화
# [('A', <itertools._grouper object at 0x7ff30fe5b9a0>), ('B', <itertools._grouper object at 0x7ff30fe5bc70>), ('C', <itertools._grouper object at 0x7ff30fe5bcd0>), ('D', <itertools._grouper object at 0x7ff30fe5bd00>), ('E', <itertools._grouper object at 0x7ff30fe5bd30>)]
gen9 = itertools.groupby('AABCCDDEE')
# print문으로 gen9 실행 시 뒤에 for문 동작 안함
# print(list(gen9))

# A:  ['A', 'A']
# B:  ['B']
# C:  ['C', 'C']
# D:  ['D', 'D']
# E:  ['E', 'E']
# 반복되는 것을 집합으로 만들어서 하나의 리스트로 가짐
for chr, group in gen9:
    print(chr, ' : ', list(group))
