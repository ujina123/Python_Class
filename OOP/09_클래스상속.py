'''
상속(inheritance)
부모클래스(super class) : 상속을 해주는 클래스
자식클래스(sub class)
'''

# 자동차 클래스
class Car:
    speed = 0
    color = ''
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 주행합니다.')

class Truck(Car):
    def __init__(self,speed,color,load):
        super().__init__(speed,color)
        self.load = load

    # Car Class(슈퍼클래스)에 있던 메소드를 재정의 (오버라이딩)
    def drive(self):
        print(f'{self.speed}의 속도로 {self.load}양의 짐을 싣고 주행합니다.')

    def loading(self):
        print(f'최대 {self.load}양의 짐을 싣고 운반할 수 있는 트럭')

# 서브 클래스 Vehicle
class Vehicle(Car):
    def __init__(self,speed,color,seat):
        super().__init__(speed,color)
        self.seat = seat

    # 슈퍼클래스에 있던 메소드를 재정의 (오버라이딩)
    def drive(self):
        print(f'{self.speed}의 속도로 {self.seat}인의 사람이 타고 주행합니다.')

truck1 = Truck(10, 'red', 1000)
truck1.drive()
truck1.loading()

car = Vehicle(10, 'red', 4)
car.drive()

## 연습 문제
# 사람클래스와 이를 상속받은 학생 클래스 정의
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def __init__(self,name,age,department, grade):
        super().__init__(self,name,age)
        self.department = department
        self.grade = grade

    def study(self):
        print(f'저의 점수는 {self.grade}점입니다.')