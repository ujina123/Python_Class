# 제어문 (if문, for문)
# 예제문제1
pw = int(input('비밀번호 입력: '))
PW = 1234

if pw == PW:
    print('비밀번호가 일치합니다.')
else:
    print('비밀번호가 일치하지 않습니다.')

if pw == PW:
    print('비밀번호가 일치합니다.')
else:
    pass

# 연습문제1 : 정수를 입력 받아서 홀수인지 짝수인지 판별하여 출력
integer = int(input("정수를 입력하세요: "))
if integer % 2 == 1:
    print("정수 %d는 홀수입니다." % integer)
elif integer % 2 == 0:
    print("정수 %d는 짝수입니다." % integer)

# 입력한 정수가 음수, 0, 양수 인지를 확인하여 출력
if integer > 0:
    print('양수')
else:
    if integer == 0:
        print('0')
    else:
        print('음수')
    pass

# 연습문제2 : 아이디,비밀번호가 입력받아서 두가지 모두 맞으면 로그인 성공
ID = 'multicampus'
PW = 1234

id = input('id : ')
pw = int(input('pw : '))

if id == ID and pw == PW:
    print("로그인 성공")
else:
    print('로그인 실패')

# 문제 : 점수를 입력받아서 학점 출력 A,B,C,D,F
score = int(input("점수 : "))
if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else:
    print("학점 F")

#######################################################

# 연습문제 1
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))
num3 = int(input("정수3 입력 : "))

num_max = max(num1,num2,num3)
print('제일 큰 수 : %d' %num_max)
# print('제일 큰 수 : {}'.format(num_max))

if num1 > num2 and num1 > num3 :
    max_num = num1
elif num2 > num3 :
    max_num = num2
else :
    max_num = num3
print('제일 큰 수 : %d' %max_num)

# 연습문제 2
figure = int(input("도형 입력(1:사각형, 2:삼각형, 3:원) : "))
if figure == 1:
    width = int(input("가로 입력 : "))
    vertical = int(input("세로 입력 : "))
    print("사각형의 면적 = %.2f" %(width*vertical))
elif figure == 2:
    base = int(input("밑변 입력 : "))
    height = int(input("높이 입력 : "))
    print("삼각형의 면적 = %.2f" %((base*height)/2))
else:
    radius = int(input("반지름 입력 : "))
    PI = 3.141592
    print("원의 면적 = %.2f" %((radius**2)*PI))

