# 필드 이용 메소드
class Car:
    model = '' # 필드, 전역변수
    def __init__(self,speed,color,model): # 생성자
        self.speed = speed
        self.color = color
        self.model = model

    # 필드 값을 반환 하는 메소드
    def getModel(self):
        return self.model

    # 필드값을 변경하는 메소드
    def setModel(self, model):
        self.model = model

    def getspeed(self):
        return self.speed

    def setspeed(self,speed):
        self.speed = speed

    def getcolor(self):
        return self.color

    def setcolor(self,color):
        self.color = color

mycar = Car(0,'red','아우디')
print(mycar.getcolor()) # 'red'

print(mycar.getModel()) # '아우디'
mycar.setModel('벤츠')
print(mycar.getModel()) # '벤츠'
print(mycar.model) # model 필드는 전역변수라서 이렇게 호출 가능