# 예외처리 (Exception)
# 에러 종류와 상관없이 에러가 발생하면 처리하기
'''
예외처리 형식
try:
    에러가 발생할 문장들
except 예외처리클래스 as e:
    에러가 발생하면 처리하는 코드들
else:
    에러가 발생하지 않으면 처리하는 문장
finally:
    에러와 상관없이 항상 수행하는 문장
'''

# 에러의 종류와 상관없이 에러를 처리하는 경우
# 예제. 0으로 나누는 경우 처리
try:
    # print(10/0)
    print('나이 : ' + 23 + '살')
except:
    # print('0으로 나눌수 없습니다.')
    print('오류발생')

# 에러 종류 명시 처리
try:
    print(10/0)
except ZeroDivisionError as e: # e : 에러 메세지 변수
    print(e)
    print('0으로 나눌 수 없습니다.')

# ValueError
try:
    num = int(input('숫자를 입력하세요 '))
except ValueError as e:
    print(e)
    print('숫자가 아닙니다.')

# 아래와 같이 사용시, 첫번째 에러만 처리가 된다.
try:
    print(10/0)
    print('나이 : ' + 23 + '살')
except ZeroDivisionError as e: # e : 에러 메세지 변수
    print(e)
    print('0으로 나눌 수 없습니다.')
except TypeError as e:
    print('형식이 잘못 지정되었습니다.', e)

try:
    print(10/0)
    print('나이 : ' + 23 + '살')
except (ZeroDivisionError,TypeError) as e: # e : 에러 메세지 변수
    print('오류가 발생했습니다.',e)


# 파일을 열었을 때 없다면 pass로 넘어가고, 에러가 발생하지 않는다면 else문 실행된다.
path = './Exception'
try:
    f = open(path+'/test.txt','r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('End----')