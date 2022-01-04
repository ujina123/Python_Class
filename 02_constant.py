'''
constant (상수)
1. 값이 변하지 않음
2. 변수와 구분하기 위해 대문자로 사용
3. 나중에 값 변경 가능 : 오류 없음
'''


# 원의 둘레와 면적을 만드는 공식
PI = 3.141592

radius = 10
area = radius * radius * PI
print(area)  # 314.1592

# 이자 계산 예제
RATE = 0.03

deposit = 100000
interest = deposit * RATE
balance = deposit * RATE
print(int(balance)) # 3000
print(format(int(balance),',')) # 천단위로 구분  3,000