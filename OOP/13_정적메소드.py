'''
정적 메소드 (static method)
인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
- 메소드 위에 @staticmethod를 붙인다.
- 메소드에 self를 넣지 않는다.
'''
class Calc:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def mul(a,b):
        return a*b

calc1 = Calc()
calc2 = Calc()
print(calc1.add(3,2))
print(calc2.add(3,2))

# 인스턴스를 생성하여 메서드를 호출하지 않고 클래스이름으로 메소드 호출
# 정적메소드 호출방식 : 클래스이름.정적메소드(*args)
print(Calc.add(10,30))
print(Calc.mul(10,30))