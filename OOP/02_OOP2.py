'''
< 자동차 클래스 >
- 기능(동작) => 메소드(함수) : 주행하다, 회전하다
- 속성(상태,값) => 변수 정의 : color, price, model, seats

< 클래스 구현과정 >
- 1단계 : 클래스 정의(선언)

class 클래스명:
    def __init__(self):
        self.필드명1 = 초기값
        self.필드명2 = 초기값

    def 메소드명1(self,매개변수,...):
        pass

    # 메소드 정의는 함수를 정의하는 것과 동일

- 2단계 : 객체 생성 (인스턴스 생성), 변수선언과 비슷
객체 변수명 = 클래스명()

- 3단계 : 객체 이용, 메소드, 필드값 변경, 필드값 사용
변수나 함수와 다르게 구별하기 위해서
객체이름.변수명
객체이름.메소드명

< 객체와 인스턴스 >
객체 : 객체만 지칭할 때는 객체 (object)라고 하고
인스턴스 : 클래스와 연관지어서 부를때를 의미한다.

self : 인스턴스가 사용하는 것 (자신)
       기존의 함수와 구분
'''

# < 자동차 클래스 >
# 기능(동작) => 메소드(함수) : speedUP(), speedDown()
# 속성(상태,값) => 변수(필드) : color, speed

## 1. 클래스 선언
# 클래스이름 : 식별자 규칙에 정의, 대문자로 시작
# 방법 1
class Car: # 사용자 정의 클래스
    def __init__(self):
        self.color = 'red'
        self.speed = 0

    def speedUP(self):
        pass

    def speedDown(self):
        pass

# 방법 2
class Car: 
    def speedUP(self):
        pass

    def speedDown(self):
        pass

# 방법 3
class Car: 
    color = 'blue'
    speed = 0

    def speedUP(self):
        self.speed += 10

    def speedDown(self):
        pass

## 2. 객체(인스턴스) 생성
myCar = Car()
yourCar = Car()

## 3. 객체(인스턴스) 사용
myCar.speedUP() # 메서드 호출 : 인스턴스.메서드()
print(myCar.color)
myCar.color = 'black'
print(myCar.color)

# 인스턴스 생성 후, 필드 추가
myCar.color = 'black'
myCar.speed = 0

# 특정한 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)
print(isinstance(myCar, Car))

## 파이썬이 기본적으로 제공하는 클래스들
# int, float, str, bool, list, dict, set, tuple,...

a = int(10)
print(type(a))

b = list(range(10))
print(type(b))

c = dict(x = 10, y = 20)
print(type(c))

e = str(10)
print(type(e))


## 연습
class Dog:
    def __init__(self,Breed,Size,Age,Color):
        self.Breed = Breed
        self.Size =Size
        self.Age = Age
        self.Color = Color

    def eat(self):
        print(f'{self.Breed} 가 밥을 먹고 있어요')
    def sleep(self):
        print(f'{self.Age} 살인 {self.Breed}는 지금 잠들었어요')
    def sit(self):
        print(f'{self.Color} 의 {self.Breed}는 앉았어요')
    def run(self):
        print(f'{self.Size} 한 {self.Breed}가 뛰어요')

dog_1 = Dog("Neapolitan Mastiff","Lage",5,"Black")
dog_1.eat() # Neapolitan Mastiff 가 밥을 먹고 있어요
dog_2 = Dog("Maltese","Small",2,"White")
dog_3 = Dog("Chow Chow","Midium",3,"Brown")