'''
앞에서 작성한 Dog 클래스에서
1. 객체간의 크기를 비교하는 메서드를 작성
2. 객체간의 나이를 더하고 빼고 곱하고 나누는 메서드 작성
'''
class Dog:
    def __init__(self,Breed ='',Size =0,Age=0,Color=''): # 디폴트 매개변수를 갖는 생성자를 만들어주었고
        self.__Breed = Breed
        self.Size = Size
        self.Age = Age
        self.Color = Color

    def getInfo(self, info=''):
        if info == 'Breed': return self.__Breed
        elif info == 'Size': return self.Size
        elif info == 'Age': return self.Age
        elif info == 'Color': return self.Color
        elif info == '': return f'\nBreed : {self.__Breed}\nSize : {self.Size}\nAge : {self.Age}\nColor : {self.Color}'

    def setInfo(self, info, modify):
        if info == 'Breed': self.__Breed = modify
        elif info == 'Size': self.Size = modify
        elif info == 'Age': self.Age = modify
        elif info == 'Color': self.Color = modify

    def eat(self,food='사료'):
        print(f'{self.__Breed}가 {food}을 먹고 있어요')

    def sleep(self,time = '지금'):
        print(f'{self.__Breed}는 {time} 잠들었어요')

    def sit(self, where = '바닥'):
        print(f'{self.__Breed}는 {where}에 앉았어요')

    def run(self, place = '길'):
        print(f'{self.__Breed}가 {place}에서 뛰고있어요')

    def __add__(self,other):
        return self.Age + other.Age

    def __sub__(self,other):
        return self.Age - other.Age

    def __mul__(self, other):
        return self.Age * other.Age

    def __divmod__(self, other):
        return self.Age / other.Age

    def __gt__(self, other):
        return self.Size > other.Size

    def __ge__(self, other):
        return self.Size >= other.Size

    def __lt__(self, other):
        return self.Size < other.Size

    def __le__(self, other):
        return self.Size <= other.Size


dog_1 = Dog(Breed ='Maltese',Size =1,Age=23,Color='white')
dog_2 = Dog(Breed ='Maltese',Size =5,Age=13,Color='white')
