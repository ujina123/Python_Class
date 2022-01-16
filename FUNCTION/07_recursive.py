# 재귀호출 : 자기함수 호출

# 문제1. 팩토리얼 계산
# for문 사용
# 3! = 3*2*1
def factorial(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

n = int(input("숫자 입력 : "))
print(f'{n}! = {factorial(n)}')

def factorial_1(n):
    fac = 1
    for i in range(n,0,-1):
        fac *= i
    return fac

n = int(input("숫자 입력 : "))
print(f'{n}! = {factorial_1(n)}')

'''
n! = n*(n-1)!
(n-1)! = (n-1)*(n-1)!

fac(n) = n * fac(n-1)
fac(n-1) = n-1 * fac(n-1-1)
fac(n) = n * (n-1) * (n-2) * ... * 1
'''

# 재귀함수
def factorial_re(n):
    if n == 1:
        return 1
    else:
        return n *factorial_re(n-1)

n = int(input("숫자 입력 : "))
print(f'{n}! = {factorial_re(n)}')

# 문제2. 카운트다운
# 반복문 이용
def count(number):
    for i in range(number,-1,-1):
        if i == 0:
            print (0)
        else:
            print(i, end=' , ')
count(10)

# 재귀함수 사용
def selfCount(number):
    if number == 0:
        print(0)
    else:
        print(number, end=' , ')
        return selfCount(number-1)
selfCount(10)