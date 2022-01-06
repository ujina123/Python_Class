'''
< 생성자 (constructor) >
- 인스턴스 생성
- 필드값을 초기화 함수

< 생성자의 형식 >
1. 생성자를 정의할 때 : __init__()
2. 생성자를 호출 (사용) 할 때 == 인스턴스(객체)를 만든다 : 클래스 이름과 같게 사용

class 클래스명:
    def __init__(self,*args):
        < 이부분에서 필드 초기화 코드 입력 >

< self >
- 클래스에서 생성된 인스턴스에 접근(인스턴스 자신)
- 인스턴스가 생성된 후 해당 인스턴스 이름으로 값을 할당하거나 메소드 호출
- 클래스 내에서 self 호출
- 생성된 인스턴스의 이름과 클래스 내의 self는 같은 역할을 한다. 
- 메소드 호출 할 때도 인스턴스의 이름과 메소드명으로 호출 

< 생성자의 종류 3가지 >
1. 기본 생성자 : 생성자에 self만 있고, 다른 매개변수가 없음
class 클래스명:
    def __init__(self): 
        pass

2. 매개변수가 있는 생성자 
class 클래스명:
    def __init__(self, *args):
        pass

3. 디폴트 매개변수 있는 생성자
class 클래스명:
    def __init__(self, arg1 = val1, arg2 = val2 ,...):
        pass

< etc >
1. _ : 변수에 특별한 의미를 부여하지 않고 사용하려고 할 때 
    ex) [print('hello') for _ in range(10)]
2. __ ( _ 2개 사용 ) : 특수한 예약함수 (메소드), 변수에 사용
    ex) if __name__ == '__main__': pass
'''

## 1. 기본 생성자
class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'red'

car1 = Car()
print(f'현재 자동차의 색상은 {car1.color}')
print(f'현재 자동차의 속도는 {car1.speed}')

## 2. 매개변수가 있는 생성자
class Car1:
    def __init__(self,speed, color):
        self.speed = speed
        self.color = color

# car2 = Car1() : 매개변수(인수)를 지정해 주지 않아서 TypeError 발생
car2 = Car1(20,'black')
print(isinstance(car2, Car1)) # True
print(f'현재 자동차의 색상은 {car2.color}')
print(f'현재 자동차의 속도는 {car2.speed}')

# 3. 디폴트 매개변수가 있는 생성자 
class Car2:
    def __init__(self,speed=0, color='yellow'):
        self.speed = speed
        self.color = color

car2 = Car2()
print(f'현재 자동차의 색상은 {car2.color}')
print(f'현재 자동차의 속도는 {car2.speed}')

car2 = Car2(20,'black')
print(isinstance(car2, Car2)) # True
print(f'현재 자동차의 색상은 {car2.color}')
print(f'현재 자동차의 속도는 {car2.speed}')


## 메소드 불러오기
class Car3:
    def __init__(self,color='red',speed=0):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 50

    def speedUP(self):
        self.speed += 10
        

if __name__ == 'main':
    mycar4 = Car3()
    print(f'초기속도 : {mycar4.speed}')
    mycar4.drive()
    print(f'drive속도 : {mycar4.speed}')
    mycar4.speedUP()
    print(f'speedUP속도 : {mycar4.speed}')