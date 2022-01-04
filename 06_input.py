num1 = int(input('숫자1 :'))
num2 = int(input('숫자2 :'))
result = num1 + num2
print('합 : ', result)
result = num1 - num2
print('차 : ', result)
result = num1 * num2
print('곱 : ', result)
result = num1 / num2
print('나누기 : ', result)

# 연습문제1
kor = int(input("국어점수 입력: "))
eng = int(input("영어점수 입력: "))
math = int(input("수학점수 입력: "))
scores = [kor,eng,math]
score_sum = sum(scores)
score_avg = score_sum / len(scores)

print("총점 : %d\n평균 : %.2f" %(score_sum,score_avg))
print('총점 : %d' %score_sum)
print('평균 : {.2f}'.format(score_avg))

# 연습문제 2
# BMI 지수 계산식 : 몸무게 / (키 * 키)
weight = float(input("몸무게(kg): "))
hight = float(input("키(미터): "))

BMI = weight / (hight ** 2)
print("당신의 BMI는 %f 입니다." %BMI)
print('당신의 BMI는 {:.2f} 입니다.'.format(BMI))