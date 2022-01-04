# format() 함수
# 포멧 형식 : format(실수, '전체자리수.소수이하자리수<서식기호>')

# 실습 ) 총점과 평균을 구해서 출력
kor = 90
eng = 80
math = 80

# 총점 : 250 , 평균 : 83.33 으로 출력
score_sum = sum([kor,eng,math])
score_average = score_sum/3
print('총점 : %d점, 평균 : %.2f점' % (score_sum, score_average))
# 포맷 형식 : format(실수, '전체자리수.소수이하자릿수<서식기호>')
print(format('총점 : %d점, 평균 : %.2f점' % (score_sum, score_average)))

print(format('총점 : {0}점, 평균 : {1:5.2f}점' .format(score_sum, score_average)))

# .format() 함수와 {}를 사용하여 서식 지정

print(format(1234.567, '10.2f'))
print('name:{}, phone:{}'.format('이유진','123-456'))
# 중괄호 안에 순서를 지정해주지 않으면 디폴트 값으로 순서대로 입력되어진다.
print('name:{1}, phone:{0}'.format('123-456','이유진'))

print('{0:d}, {1:d}'.format(100,123))
print('{1:d}, {0:d}'.format(100,123))
print('{1:d} {0:5d} {0:10d}'.format(123,123,123))
print('%d %5d %10d'%(123,123,123))