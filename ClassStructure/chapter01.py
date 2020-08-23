import random
import abc
from collections.abc import Sequence
import timeit


class VectorP:
    # 생성할 때는 조건 만들어 놓으면 체크하지만 밖에서 수정하는 경우 체크 못함
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # Generator

    # Getter / Setter
    # 주로 함수이름은 변수이름으로 함
    # get method
    @property
    def x(self):
        print('Called Property x getter')
        return self.__x

    @x.setter
    def x(self, v):
        print('Called Property x setter')
        self.__x = float(v)

    @property
    def y(self):
        print('Called Property y getter')
        return self.__y

    @y.setter
    def y(self, v):
        if v < 30:
            raise ValueError('30 Below is NOT POSSIBLE')
        print('Called Property y setter')
        self.__y = float(v)


# 객체 선언
v = VectorP(20, 40)
# __ 사용하면 감춰져있음. 직접 접근 안됨
# print(v.__x, v.__y)
print(v.x)  # 정상 동작
v.x = 10
v.y = 40
print(v.x)
print(v.y)

# Iter 확인
for val in v:
    print(val)


# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용

class TestA:
    __slots__ = ('a',)


class TestB:
    pass


use_slot = TestA()
no_slot = TestB()

print(use_slot)
# AttributeError: 'TestA' object has no attribute '__dict__'
# print(use_slot.__dict__)
print(no_slot)
# {}
print(no_slot.__dict__)

# 메모리 사용량 비교

# 측정을 위한 함수 선언


def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner


# 0.00018281700000000178 -> 더 빠름(메모리 덜 사용)
print(min(timeit.repeat(repeat_outer(use_slot), number=1000)))
# 0.00025694399999999853
print(min(timeit.repeat(repeat_outer(no_slot), number=1000)))

# 객체 슬라이싱


class Objects:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]


s = Objects()
# print(s.__dict__)
# print(len(s))
# print(len(s._numbers))
# print(s[1:100])
# print(s[-1])
# print(s[::10])

# 추상 클래스 (ABC)

# 개발과 관련된 공통된 내용 (필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것
# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함

# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contain__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜


class IterTestA():
    def __getitem__(self, idx):
        # range(1,50,2)
        return range(1, 50, 2)[idx]


i1 = IterTestA()

# 9
# range(9, 21, 2) - iter 작동
# True - contain 작동
print(i1[4])
print(i1[4:10])
print(3 in i1[1:10])
# print([i for i in i1])


# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작


class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])


# TypeError: Can't instantiate abstract class IterTestB with abstract methods __len__
# __len__ 구현해줘야 작동
i2 = IterTestB()
print(i2[4])
print(i2[4:10])
print(3 in i2[1:10])

# abc 활용 예제

# metaclass=abc.ABCMeta (3.4 이하)
# __metaclass__ = abc.ABCMeta


class RandomMachine(abc.ABC):
    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        """Iterable 항목 추가"""

    # 추상 메소드
    @abc.abstractclassmethod
    def pick(self, iterobj):
        """무작위 항목 뽑기"""

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:  # 찾는게 없는 경우
                break
            return tuple(sorted(items))


class CraneMachine(RandomMachine):
    def __init__(self, items):
        # systemtimestamp 사용하여 더 다양하게 랜덤 값 추출
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self):
        return self.pick()


# 서브 클래스 확인
# 뒤에 것이 부모
print(issubclass(RandomMachine, CraneMachine))
print(issubclass(CraneMachine, RandomMachine))

# 상속 구조 확인
# (<class '__main__.CraneMachine'>, <class '__main__.RandomMachine'>, <class 'abc.ABC'>, <class 'object'>)
print(CraneMachine.__mro__)

# 추상 메소드 구현 안하면 에러 발생
cm = CraneMachine(range(1, 100))
print(cm._items)
print(cm.pick())
print(cm())
# 자식에는 없지만 부모에 있어서 사용 가능
print(cm.inspect())
