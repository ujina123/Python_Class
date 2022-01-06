'''
< 비공개 필드와 메소드 생성 >
비공개 필드 :필드를 외부에서 직접 사용하지 못하도록 하는 방법
          클래스 내부에서만 사용가능
          사용 방법 : __필드명

비공개 메소드 : 외부에서 직접 사용하지 못하고 클래스 내부에서만 접근
            형식 : def __메소드명(self,*args)
'''
class Car:
    def __init__(self,speed = 0, color = 'white'):
        self.speed = speed
        self.__color = color # 클래스 내에서만 사용하는 비공개 필드

    def getcolor(self):
        return self.__color

    def setcolor(self,color):
        self.__color = color

# 비공개 필드에 접근하려면 필드를 이용하는 메소드를 정의하여 호출
car1 = Car()
print(car1.speed)
# print(car1.color) -> AttributeError: 'Car' object has no attribute 'color'
print(car1.getcolor())
car1.setcolor('red')
print(car1.getcolor())

# 비공개 메소드
class Car:
    def __init__(self,modelN ,speed = 0, color = 'white'):
        self.modelN = modelN
        self.speed = speed
        self.__color = color # 클래스 내에서만 사용하는 비공개 필드

    def __modelN(self): # 클래스 내에서만 사용하는 비공개 메소드
        print(self.modelN)

    def getcolor(self):
        return self.__color

    def setcolor(self,color):
        self.__color = color

    def printInfo(self):
        self.__modelN()
        print(self.getcolor())

car1 = Car('1234-454')
car1.printInfo()
