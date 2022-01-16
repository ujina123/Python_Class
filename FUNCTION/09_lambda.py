# lambda(람다)함수 : 함수를 한줄로 간단하게 작성
# 변수 = lambda 매개변수들: 식

def add(x,y):
    result = x+y
    return result

print(add(10,20))

add2 = lambda x,y : x+y
print(add2(10,20))

# 매개변수에 기본값을 설정
add3 = lambda x=10,y=10 : x+y # 디폴트 매개변수 예시
print(add3(10,20))
print(add3())

print('-'*30)
def add10(num):
    for n in range(len(num)):
        print(num[n] + 10)

num = [10,20,30,40]
add10(num)

def add10(num):
    return num + 10

lambda num: num+10

for i in range(len(num)):
    num[i] = add10(num[i])
print(num)

# map()함수
num2 = list(map(add10,num))
print(num2)

# lambda() & map()
num3 = list(map(lambda num: num+10,num2))
print(num3)

# (lambda 매개변수들: 식)(인수)
# 람다 표현식을 변수에 할당하지 않고 그 자페를 호출해서 사용
(lambda x : x+10)(25)

# 람다 표현식안에서 변수 생성 불가
# (lambda x,y=10: x+y)(5) => error

y = 10
(lambda x,y=10: x+y)(5)