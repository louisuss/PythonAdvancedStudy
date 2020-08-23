# id VS __eq__ (==) 증명
import copy
x = {'name': 'Kim', 'age': 33, 'city': 'Seoul'}
y = x

print(id(x), id(y))
print(x == y)
print(x is y)
print(x, y)
x['class'] = 10
print(x, y)

z = {'name': 'Kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print(x, z)
# 같은 객체
# False
print(x is z)

# 값 비교
# True
print(x == z)

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교
# id 값 같은지를 먼저 비교 후 값 비교

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])
# False
print(tuple1 is tuple2)
# True
print(tuple1 == tuple2)
print(tuple1.__eq__(tuple2))

# Copy, Deepcopy

# copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

# True
print(tl1 == tl2)
print(tl1 is tl2)
print(tl3 == tl1)

# False
print(tl3 is tl1)

tl1.append(1000)
tl1[1].remove(105)

# [10, [100], (5, 10, 15), 1000]
print(tl1)
print(tl2)
# [10, [100], (5, 10, 15)]
print(tl3)

tl1[1] += [110, 120]
tl1[2] += (110, 120)

# [10, [100, 110, 120], (5, 10, 15, 110, 120), 1000]
print(tl1)
# 리스트 안에 튜플 사용은 위험
# 튜플 재 할당 (객체 새로 생성) - 불변이기 때문
print(tl2)

# [10, [100, 110, 120], (5, 10, 15)]
print(tl3)


# Deepcopy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


b1 = Basket(['Apple', 'Bag', 'TV', 'Snack'])
b2 = copy.copy(b1)
b3 = copy.deepcopy(b1)

# 140259661033728 140259661033920 140259661035264
# 값 다름
print(id(b1), id(b2), id(b3))

# 140277529959552 140277529959552 140277529957696
# 그냥 카피는 값 같음
# 같은 객체를 참조
print(id(b1._products), id(b2._products), id(b3._products))

b1.put_prod('Orange')
b2.del_prod('Snack')
print(b1._products)
print(b2._products)
print(b3._products)

# 함수 매개변수 전달 사용법


def mul(x, y):
    # x = x+y 결과와 같음
    x += y
    return x


x = 10
y = 5

print(mul(x, y))

a = [10, 100]
b = [5, 10]

# [10, 100, 5, 10] [10, 100, 5, 10] [5, 10]
# a 원본도 변경됨
print(mul(a, b), a, b)  # 가변형 -> 데이터 변경

c = (10, 100)
d = (5, 10)

# (10, 100, 5, 10) (10, 100) (5, 10)
print(mul(c, d), c, d)  # 불변형 -> 데이터 변경 안됨

# 파이썬 불변형 예외
# str, bytes, frozenset, tuple: 사본 생성 x -> 참조 반환
tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

# True
# 140491792109872 140491792109872
# 참조 반환
print(tt1 is tt2)
print(id(tt1), id(tt2))

# True
# 140590234521904 140590234521904
print(tt1 is tt3)
print(id(tt3), id(tt1))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

# True True 140511748237808 140511748237808
# 참조 반환
print(tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))

# True True 140228824612784 140228824612784
# 참조 반환
print(ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
