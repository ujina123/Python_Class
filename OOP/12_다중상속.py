'''
다중상속 : 여러클래스에서 상속을 받음
형식)
class 클래스이름(부모클래스1,부모클래스2, ...):
        pass

다중상속 : 다이아몬드 상속의 예
        동일한 이름의 메소드를 갖는 경우
메소드 탐색 순서(Method Resolution order:MRO) 규칙에 따라 처리 
- .mro() 실행
'''

class Person:
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"안녕하세요 {self.name}님")

class University:
    def __init__(self,department='', grade=''):
        self.department = department
        self.grade = grade

    def manageScore(self):
        print("학점관리")

class Undergraduate(Person,University):
    def study(self):
        print("공부하기")

kim = Undergraduate()
kim.name = 'kim'
kim.age = 20
kim.greeting()
kim.manageScore()
kim.study()


class A: # A(object)
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeitng(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C):
    pass

X = D()
X.greeting() # 안녕하세요 B입니다.
X.greeitng() # 안녕하세요 C입니다.

# 클래스.mro()를 이용하여 메소드 호출 순서 확인
print(D.mro())