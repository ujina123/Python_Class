'''
클래스메소드
- 인스턴스를 통하지 않고 메소드를 클래스에서 바로 호출해서 사용
- 매소드내에서 클래스 변수, 클래스 ...(강의녹화 찾아보기)
- @classmethod를 메소드 위에 붙임
- 메소드 인수로 self 대신 cls를 지정 (cls == class)
형식 )
class 클래스이름:
    @classmethod
    def 메소드명(cls ,매개변수들):
        문장들

호출 형식 )
클래스이름.메소드명(인수들)
'''

# 클래스변수 이용 예시)
class Person:
    count = 0 # 클래스변수
    def __init__(self,name):
        self.name = name
        Person.count += 1

    def printCount(self):
        print(f'{self.count}명이 태어났습니다.')

man1 = Person('Kim')
man1.printCount()
man2 = Person('Lee')
man2.printCount()

# @classmethod
class Person:
    count = 0 # 클래스변수
    def __init__(self,name):
        self.name = name
        Person.count += 1

    @classmethod
    def printCount(cls):
        print(f'{cls.count}명이 태어났습니다.')

man1 = Person('Kim')
Person.printCount()
man2 = Person('Lee')
Person.printCount()