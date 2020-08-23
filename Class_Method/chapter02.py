from copy import deepcopy

# 클래스 변수와 인스턴스 변수 차이

# 클래스 재 선언


class Student():
    """
    Student Class
    Author : louis
    Date : 2020.07.10
    """

    # 클래스 변수 : 모두가 공유
    student_cnt = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_cnt += 1

    def __str__(self):
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'repr: {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(
            self._name, self._email, self._details))

    # 직접 구현 안함. 파이썬 내부적으로 알아서 처리해줌.
    def __del__(self):
        Student.student_cnt -= 1


# Self 의미
std1 = Student('Cho', 2, 3, {'gender': 'Male', 'score': 90})
std2 = Student('Lee', 2, 3, {'gender': 'Female',
                             'score': 95}, 'dobi@gmail.com')
std3 = deepcopy(std1)
std4 = std1

# id 확인
print(id(std1))
print(id(std2))
print(id(std3))
print(id(std4))

# Id 값 비교
print(std1 is std3)  # False
# 값 비교
print(std1 == std3)  # False
print(std1 == std4)  # True

# dir & dict 확인
# 1. dict 확인 (클래스 속성값만 확인) 2. dir 확인 (자세함)
print(dir(std1))
print(std1.__dict__)

# Docstring : 주석 출력
print(Student.__doc__)

# 실행
std1.detail_info()
std2.detail_info()

# 에러
# 클래스라 self 없음
# Student.detail_info()

Student.detail_info(std1)

# 비교
print(std1.__class__, std2.__class__)
# True
print(id(std1.__class__) == id(std2.__class__))

# 인스턴스 변수
# 직접 접근 (PEP 문법적으로 권장X)

std1._name = 'haha'
print(std1._name)

# 클래스 변수

# 접근
print(std1.student_cnt)
print(std2.student_cnt)
print(Student.student_cnt)

# 공유 확인
print(Student.__dict__)
# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
print(std1.__dict__)

del std2
print(std1.student_cnt)
print(Student.student_cnt)