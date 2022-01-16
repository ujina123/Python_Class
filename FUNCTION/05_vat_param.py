'''
[ 가변 길이 매개변수 ]
- 매개변수의 개수가 정해져 있지 않은 경우
- 여러 개의 값을 전달 받아 사용할 경우
- *args : arguments의 약자, 인수 값을 받음
- **kwarge : keyWord arguments의 약자, key = value값을 받음

[ 위치 인수와 키워드 인수 ]
- 위치에 의해 인수를 구별하는 방식 : 기본
   print(sum(10,20,30))
- 키워드 인수 전달
   print(sumM(a = 10, c = 30, b = 20))
   print(sumM(a = 10, b = -10, c = 50))
'''

# 예제1) *args형식을 이용하여 여러 개 인수의 값을 더하는 함수
def sumN(*args):
    total = 0
    for x in args:
        total += x
    return total

print(sumN(1,2,3))
print(sumN(1,2,3,4,5))
print(sumN(1,2,3,4,5,6,7))

# 예제2) *매개변수 형식을 사용하여 이름 인수 
def showNames(*names):
    for n in names:
        print(n,end=' ')
    print( )

showNames('홍길동','강감찬')
showNames('홍길동','강감찬','유관순','이순신')

# 예제3) **kwargs 예제 : 키 = 값
def showInfo(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print('\n')
    for value in kwargs.values():
        print(value, end=' ')
    print('\n')
    for item in kwargs.items():
        print(item)

showInfo(name = '홍길동', id = '123', phone = '010-1234-1234', address = '서울시 서초구 삼성동')
showInfo(name = 'sun', id = 'moon')