'''
인스턴스(instance)변수 : 필드
'''

# 클래스 변수 : 여러 인스턴스가 공유하는 변수
class Car:
    color = ""
    speed = 10
    count = 0  # 클래스 변수

    def __init__(self):
        self.speed = 0
        Car.count += 1 # 클래스 변수
        print(f'현재 총 {Car.count}번째 자동차가 생산되었습니다.')

car1 = Car()
# print(car1.count)
print(Car.count)
car2 = Car()
car1.speed # 인스턴스 변수 : 필드
car2.speed

# print(car1.count)
# print(car2.count)
print(Car.count) # 클래스 변수

car2 = Car()
print(Car.count)