# Class Method / Instance Method / Static Method

# Instance Method
class Student():
    """
    Student Class
    Author : louis
    Date : 2020.07.10
    Description : Class, Static, Instance Method
    """
    # class variable
    tuition_rate = 1.0

    # 생성자
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # instance method
    # 첫번째 인자로 self가 들어감
    def full_name(self):
        return self._first_name + ' ' + self._last_name

    def detail_info(self):
        return 'Student Detail Info: {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    def get_fee_cal(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_rate)

    def __str__(self):
        return 'Student Info -> name: {}, grade: {}, email: {}'.format(self.full_name(), self._grade, self._email)

    # class method
    # 클래스 객체를 활용해서 사용하는 메소드는 class decorator 사용
    # cls -> class Student가 넘어옴. 클래스 자체
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter more than 1')
            return
        else:
            cls.tuition_rate = per
            print('Success')

    @classmethod
    def student_create(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition*cls.tuition_rate, gpa)

    # 누구나 사용할 수 있는 메소드
    # static method
    # class method, instance method 아니면 클래스와 밀접한 함수이면 static method를 사용하라 권장
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient'


# 학생 인스턴스
std1 = Student(1, 'Kim', 'Dohyun', 'std1@naver.com', '1', 400, 3.5)
std2 = Student(2, 'Lee', 'Minho', 'std2@gmail.com', '2', 500, 4.3)

# 기본 정보
print(std1)
print(std2)
print()

# 전체 정보
print(std1.detail_info())
print(std2.detail_info())
print()

# 학비 정보(인상전)
print(std1.get_fee())
print(std2.get_fee())
print()

# 학비 정보(인상후)
# 변수 직접 접근 안좋음
# Student.tuition_rate = 1.2

# 클래스 메소드 사용
Student.raise_fee(1.2)

print(std1.get_fee_cal())
print(std2.get_fee_cal())
print()

# 클래스 메소드 인스턴스 생성
std3 = Student.student_create(
    3, 'Park', 'Minji', 'std3@gmail.com', '3', 550, 4.5)
print(std3.detail_info())
print()

# 장학금 혜택 여부 (static method 미사용)


def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient'


print(is_scholarship(std1))
print(is_scholarship(std2))
print(is_scholarship(std3))
print()

# static method 호출1
print(Student.is_scholarship_st(std1))
print(Student.is_scholarship_st(std2))
print(Student.is_scholarship_st(std3))
print()

# static method 호출2
print(std1.is_scholarship_st(std1))
print(std2.is_scholarship_st(std2))
print(std3.is_scholarship_st(std3))
