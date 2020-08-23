# List & Tuple
# 컨테이너(Container): 서로 다른 자료형(list, tuple, collections.deque)
# Flat: 한 개의 자료형(str, bytes, bytearray, array.array, memoryview)
# 가변(mutable): list, bytearray, array.array, memoryview, deque
# 불변(immutable): tutple, str, bytes


# Non Comprehending Lists
from array import array
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))
print(codes1)

# 지능형 리스트(Comprehending Lists)
# 데이터가 클 경우 성능이 더 좋음
codes2 = [ord(s) for s in chars]
print(codes2)

# 40번 이상만 필요할 때
codes3 = [ord(s) for s in chars if ord(s) > 40]
print(codes3)

# Map, Filter
codes4 = list(filter(lambda x: x > 40, map(ord, chars)))
print(codes4)

print([chr(s) for s in codes1])
print()

# Generator : 반복을 하나하나 하는데 값을 생성해 냄
# 한번에 한개의 항목을 생성(메모리 유지X) -> 성능 좋음
tuple_g = (ord(s) for s in chars)
# <generator object <genexpr> at 0x7fb2dab6a510>
# next나 for문뒤에 사용하지 않으면 아직 메모리에 올리지 않음
print(tuple_g)
print(next(tuple_g))
print(next(tuple_g))

# 첫인자: 자료형 타입
array_g = array('I', (ord(s) for s in chars))
# array('I', [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43])
print(array_g)
# [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43]
print(array_g.tolist())
print()

# 제너레이터 예제
# <generator object <genexpr> at 0x7fa427562660>
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print(s)
print()

# 리스트 주의 할 점
# [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
# [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
mark1 = [['~']*3 for n in range(3)]
mark2 = [['~']*3]*3
print(mark1)
print(mark2)
print()

# [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~']]
# [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]
mark1[0][1] = 'X'
mark2[0][1] = 'X'
print(mark1)
print(mark2)

# 증명
# [140675394254272, 140675394254080, 140675394254016]
# [140675394253824, 140675394253824, 140675394253824]
print([id(i) for i in mark1])
print([id(i) for i in mark2])

# Tuple
# Packing & Unpacking

a, b = divmod(100, 9)
# 몫 나머지
print(a, b)
# (11, 1)
# (11, 1)
print(divmod(100,9))
print(divmod(*(100, 9)))

# 11 1
print(*(divmod(100, 9)))

# 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(10)
print(x, y, rest)
# 0 1 []
x, y, *rest = range(2)
print(x, y, rest)

# 1 2 [3, 4, 5]
x, y, *rest = 1,2,3,4,5
print(x, y, rest)

# *: 묶여서 패킹된 것을 안에서 언팩, **: 딕셔너리 형태로 받음
# def test(*args, **args)

# Mutable VS Immutable
l = (10,15,20)
m = [10,15,20]
# (10, 15, 20) [10, 15, 20] 140316427448064 140316427932096
print(l, m, id(l), id(m))

l = l*2
# id 바꿔서 할당하려면 이방식 써야됨. l*=2 안됨
m = m*2
# id 바뀜
# (10, 15, 20, 10, 15, 20) [10, 15, 20, 10, 15, 20] 140316427564704 140316427932032
print(l, m, id(l), id(m))

# id 바뀜
l *= 2
# id 안 바뀜(자기 리스트에 재할당) <-> m = m*2
m *= 2
# 140262705700928 140262706196928
print(id(l), id(m))

# reverse, key=len, key=str.lower, key=func
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'coconut']

# sorted: 정렬 후 '새로운' 객체 반환
# 원본 변경 안됨
print(sorted(f_list))
print(sorted(f_list, reverse=True))
print(sorted(f_list, key=len))
# 마지막 글자 기준 정렬
print(sorted(f_list, key=lambda x: x[-1]))
print(sorted(f_list, key=lambda x: x[-1], reverse=True))

# sort: 정렬 후 객체 직접 변경
# 함수 리턴이 None 이면 반환값 없는 함수
a = f_list.sort()

# None ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya']
# None ['papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
# None ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut']
# None ['coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya']
print(a, f_list)
print(f_list.sort(reverse=True), f_list)
print(f_list.sort(key=lambda x: x[-1]), f_list)
print(f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

