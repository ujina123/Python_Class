# 연습 문제 : 1부터 10까지 더하기
# = : 할당 연산자
# 대입연산자 : += -= *= /=
# x +=1 : x = x+1 (누적 더하기)
# x -=1 : x = x-1
# x +=1 : x = x+2

sumX = 0 # 초기화 : 초기값을 지정한다.
for i in range(1,11):
    sumX += i
print(sumX)

# 1~ 100까지의 홀수만 더한 결과 출력
odd_number = 0
for i in range(1,101,2):
    odd_number += i
print(odd_number)

# 문제 : 1~100사이 정수 중 홀수와 짝수의 합을 각각 구하여 출력하기
odd_number ,even_number = 0,0
for i in range(1,101):
    if i % 2 == 1: odd_number += i
    else: even_number +=i
print(odd_number, even_number)

odd,even = 0,0
for i in range(1,101,2):
    odd += i
    even += i+1
print(odd,even)

# 1 ~ 100사이의 3의 배수 출력하고 더하기
sum_num = 0
for i in range(3,101,3):
    print(i)
    sum_num += i
print(sum_num)

# 연습문제 : 구구단의 단수를 입력받아서 해당하는 구구단을 출력하기
num = int(input("단수를 입력하세요 : "))
for i in range(1,10):
    print('%d * %d = %d' %(num,i,(num*i)))
    print('{} * {} = {:2d}'.format(num, i, (num * i)))

# 연습문제 2 : 카운트 다운 프로그램
# 시작 숫자를 입력하시오 : 10
# 10 9 8 7 6 ... 1 성공
num = int(input("시작 숫자를 입력하시오 : "))
for i in range(num,0,-1):
    print(i, end=" ")
print("성공")

