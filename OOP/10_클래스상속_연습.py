'''
클래스 상속과 메소드 재정의 연습
- 다형성 (polymorphism) : 같은 이름의 메서드가 다른 기능을 할 수 있도록 한 것

Animal 클래스 정의
메소드 : talk(), eat(), sleep()
필드 : Age, leg, color, breed

Sub class _ Dog
메소드 : talk() 재정의 -> '멍멍'

Sub class _ Cat
메소드 : talk() 재정의 -> '야옹'
'''

class Animal:
    age = 0 # 클래스의 변수값
    leg = 0
    color = ''
    breed = ''
    def __init__(self,age,leg,color,breed): # 생성자 : 클래스의 객체 (인스턴스)를 만들기 위한 것
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed

    def talk(self):
        print("동물이 소리를 내고있어요")
    def eat(self):
        print("동물이 지금 무언가를 먹고 있어요")
    def sleep(self):
        print("동물이 지금 잠을 자고 있어요")
    def Info(self):
        print(f'이 동물은 {self.breed}종으로 {self.leg}개의 다리를 가지고 있고, {self.color}의 색을 띄고 있습니다.')

class Dog(Animal):
    def talk(self):
        print(f'멍멍')

class Cat(Animal):
    def __init__(self, age, leg, color, breed, hair):
        super().__init__(age, leg, color, breed)
        self.hair = hair

    def talk(self):
        print(f'야옹')

    def skin(self):
        print(f'이 고양이는 {self.hair} 털을 가지고 있어요')

animal = Animal(2,2,'blue','c')
animal.talk()

dog_1 = Dog(4,4,'red','a')
dog_1.talk()
dog_1.Info()

cat_1 = Cat(2,4,'white','b','부드러운')
cat_1.talk()
cat_1.Info()
cat_1.skin()

# 다형성
animals = [Cat(1,4,'white','A','부드러운'),Cat(1,4,'red','B','따가운'),Dog(2,4,'black','d1')]
for animal in animals:
    animal.talk()
