''' 
< format() 함수 >
포멧 형식 : format(실수, '전체자리수.소수이하자리수<서식기호>')

# '''
# % 서식 문자열

print('Name: {0}, Phone: {1}'.format('kmlee','123-445'))

name = 'kmlee'
phone = '123-1234'
s = name+phone
print(s)
s1 = '%d %5d %05d' %(123,123,123)
s2 = '{0:d} {1:5d} {2:05d}'.format(123,123,123)
print('이름은 {}이고, 폰번호는 {}이다.'.format(name,phone))
print(f'이름은 {name}이고, 폰번호는 {phone}입니다.')

# f'string
tea = 'coffee'
n = 5
s3 = f'나는 {tea}를 좋아해요. 하루에 {n}잔 마셔요.'

for month in ['1월','2월','3월']:
    print(f'이번달은 {month}입니다.')

# string.format()
# 1) '문자열 {위치인덱스}'.format(변수)
print('Name:{0}, Phone:{1}'.format('kmlee',1234-123))
s2 = '{0:d} {1:5d} {2:05d}'.format(123,123,123)

# 2) '문자열 {변수}'.format(변수 = 값)
print('이름은 {name}이고, 폰번호는 {phone}'.format(name = '이몽룡',phone = '123-111'))


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