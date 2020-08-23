# 딕셔너리 구조
# 코드 반복 지속
# 이런 구조는 많이 사용되고 있기는 함
# 데이터베이스나 기타 써드파티(외부에서 제공하는 것)에서 주로 사용
# JSON Array

student_dicts = [
    {'std_name': 'kim', 'std_num': 1, 'std_grade': 1},
    {'std_name': 'kim', 'std_num': 1, 'std_grade': 1},
    {'std_name': 'kim', 'std_num': 1, 'std_grade': 1},
]

# OOP
# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용


class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'repr: {}'.format(self._name)


student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score': 95})
print(student1.__dict__)

students_list = []

students_list.append(student1)
print(students_list)

# __str__ 때문에 이름 출력
# __str__ 없으면 __repr__ 출력
for i in students_list:
    print(i)
