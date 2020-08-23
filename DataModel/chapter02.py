# Magic Method

# 기초 설명

# 모든 속성 및 메소드 출력
print(dir(int))

n = 100
print(n + 200)
print(n.__add__(200))
print(n.__doc__)
print(n.__bool__(), bool(n))
print(n*100, n.__mul__(100))

# 클래스 예제


class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Std Class Info: {}, {}'.format(self._name, self._height)

    # overloading
    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._height - x._height


s1 = Student('James', 181)
s2 = Student('Park', 183)

# unsupported operand type(s) for +: 'Student' and 'Student'
# print(s1+s2)
# __ge__
print(s1 >= s2)
# __le__
print(s1 <= s2)
# __sub__
print(s1 - s2)


class Vector:
    def __init__(self, *args):
        """Create a vector, example : v = Vector(1,2)"""
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """Returns the vector info"""
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """Returns the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# Create a vector, example : v = Vector(1,2)
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(v1, v2, v3)
print(Vector.__add__.__doc__)
print(v1 + v2)
print(v1 * 4)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
