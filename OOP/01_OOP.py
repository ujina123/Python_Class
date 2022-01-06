'''
## 객체 지향 프로그래밍 (Object Oriented Programming)
- 함수처럼 어떤 기능을 함수 코드에 묶어두지 않고 객체에 기능을 정의 하는 것
- 함수와 변수를 함께 가질 수 있도록 구성
- 코드의 재사용성 

객체 : 함수 (function) + 데이터 (변수)
ex) TV : 끄다, 켜다, 채널 변경, 가격 ...

## 클래스 (class)
- 객체를 만들어내는 틀 (설계도)
- 객체가 가지는 기본 정보를 담은 코드
- 클래스 : 메소드(함수) + 필드(변수)

## 인스턴스 (instance)
- 클래스로부터 생성된 객체
- 실제로 생성되는 객체
'''

# 계산기 : 함수와 변수로 동작
result = 0
def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(7))
print(adder(5))

# 계산기 : class 사용
class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self,num):
        self.result += num
        return self.result

result1= Calculator()
print(result1.adder(3))
print(result1.adder(7))

result2= Calculator()
print(result2.adder(3))
print(result2.adder(7))