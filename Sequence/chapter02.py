# 해시테이블 (hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X

# Dict 구조
# 파이썬 내장함수 리스트 보여줌
# print(__builtins__.__dict__)

# Hash 값 확인 - 중복이 되는지 안되는지 허용할지 안할지 생각 가능
from unicodedata import name
from dis import dis
from types import MappingProxyType
import csv
t1 = (10, 20, (30, 40, 50))
print(hash(t1))
# 리스트가 중복 가능하므로 에러뜸
# t2 = (10, 20, [30,40,50])
# print(hash(t2))


# 외부 CSV to List of tuple

with open('./res/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print(NA_CODES)
print()

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print(n_code1)
print(n_code2)

# Dict Setdefault 예제
# 키가 중복되어 Dict 안됨
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val2'),
    ('k3', 'val3'),
    ('k4', 'val4'),
    ('k5', 'val5'),
)
new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# Use setdefault
# 키로 사용될 것들이 중복되는 구조
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)

# 사용자 정의 dict 상속(UserDict 가능)


class UserDict(dict):
    def __missing__(self, key):
        print('Called: __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called: __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('Called: __contains__')
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])

# 출력
# {'one': 1, 'two': 2}
# {'one': 1, 'two': 2}
# {'one': 1, 'two': 2}
print(user_dict1, user_dict2, user_dict3)

# Called: __getitem__
# Called: __missing__
# None
print(user_dict2.get('aaa'))

# Called: __getitem__
# 2
print(user_dict2.get('two'))

# Called: __contains__
# True
print('one' in user_dict3)

# raise KeyError(key)
# print(user_dict3['three'])
# None
print(user_dict3.get('three'))

# False
print('three' in user_dict3)
print()
print()

# Immutable Dict

d = {'key1': 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)

# {'key1': 'TEST1'} 140452816131648
# {'key1': 'TEST1'} 140452816419616
# False True
print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key1] = 'TEST2'

d['key2'] = 'TEST2'
print(d)
print()

# Set 구조(FrozenSet)
s1 = {'Apple', 'Orange', 'Apple', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Kiwi'])
s3 = {3}
s4 = set()  # Not {}
# 캡슐화
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Kiwi'})

s1.add('Melon')
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 1           0 LOAD_CONST               0 (10)
# 2 BUILD_SET                1
# 4 RETURN_VALUE
# None

# 1           0 LOAD_NAME                0 (set)
# 2 LOAD_CONST               0 (10)
# 4 BUILD_LIST               1
# 6 CALL_FUNCTION            1
# 8 RETURN_VALUE
# None

print(dis('{10}'))  # 더 빠름
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)

# name - 유니코드에 대한 설명 보여줌
print({name(chr(i), '') for i in range(0, 256)})
