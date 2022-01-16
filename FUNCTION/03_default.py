'''
디폴트 매개변수
: 매개변수의 기본값을 지정
'''

from operator import ge


def greet(name = '무명',msg = '안녕^^'):
    print(name + '!'+ msg)

greet('홍길동','빈가워') # 홍길동!빈가워
greet('홍길동') # 홍길동!안녕^^
greet() # 무명!안녕^^

def showInfo(name, year=1, age=20):
    print(name,year,age)

showInfo('홍길동',3,10) # 홍길동 3 10
showInfo('홍길동',3) # 홍길동 3 20
showInfo('홍길동') # 홍길동 1 20
