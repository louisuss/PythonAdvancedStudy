# https://docs.python.org/3/reference/datamodel.html
# 데이터 모델(Data Model)
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수, 클래스

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id(주소), type(자료형) -> value
# 파이썬 -> 일관성

# 일반적인 튜플
# 튜플 -> 변경 안됨, 속도가 리스트 보다 빠름
from collections import namedtuple
from math import sqrt
p1, p2 = (1.0, 5.0), (2.5, 1.5)

line_len = sqrt((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2)
print(line_len)

# Namedtuple
Point = namedtuple('Point', 'x y')

p1 = Point(1.0, 5.0)
p2 = Point(2.5, 1.5)

line_len2 = sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
print(line_len2)
print()

# 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')

# 똑같은 레이블, 예약어 class 사용
# rename 옵션을 통해 자동 수정
Point4 = namedtuple('Point', 'x y x class', rename=True)

print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
# temp_dict 하나를 x로 봐서 에러
# p5 = Point3(temp_dict)
# print(p5)

# **를 통해 바인딩 가능
p5 = Point3(**temp_dict)
print(p5)

print(p1, p2, p3, p4)
print()

# 사용
print(p1[0] + p2[1])  # Index Error 주의
print(p1.x + p2.y)  # 클래스 변수 접근 방식

# Unpacking
x, y = p3
print(x+y)

# Rename 테스트
print(p4)

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
# Point(x=52, y=38) - 개수를 맞춰야 함
print(p4)

# _fields : 필드 네임 확인
# ('x', 'y') ('x', 'y') ('x', 'y')
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
# {'x': 10, 'y': 35} {'x': 52, 'y': 38}
print(p1._asdict(), p4._asdict())

# _replace() : 수정된 새로운 객체 반환 - id 값이 바뀜
# Point(x=20, y=100)
print(p2._replace(y=100))

# 실습
# 학생 전체 그룹 생성
# 반20명, 4개의 반 -> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
# List Comprehension
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
# namedtuple 형태
students = [Classes(rank, number) for rank in ranks for number in numbers]

# len : 80
print(len(students))
# A
print(students[4].rank)

# 가독성 안좋은 케이스
students2 = [Classes(rank, number) for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1, 21)]]

# <generator object <genexpr> at 0x7fb5945744a0>
print(s for s in students)

for s in students:
    print(s)
