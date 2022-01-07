'''
< join() >
문자열 결합(삽입) 
각 문자 사이에 특정문자(열) 삽입하여 결합
'''
a = 'aa'
a = a.join('bbb')
print(a)

a = ','
a = a.join('1234')
print(a)

'''
< replace(찾는 문자열, 변경할 문자열) >
문자열 변경
전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경
찾는 문자열이 존재하면 변경할 문자열로 대체하여 반환
찾는 문자열이 없는 경우 원래 문자열을 반환
'''
lan = 'Python programming'
print(lan)
print(lan.replace('Python','Java'))

'''
# 공백 제거
strip() : 문자열의 앞뒤의 공백을 제거
lstrip() : 문자열의 왼쪽의 공백을 제거
rstrip() : 문자열의 오른쪽의 공백을 제거
'''
string = '  python  '
print(string.strip())
print(string.lstrip())
print(string.rstrip())

'''
< 대소문자 변경 > 
upper() : 대문자로 변경
lower() : 소문자로 변경
capitalize() : 문장의 첫번재 문자열의 첫문자를 대문자로 변환
title() : 각 단어의 첫문자를 대문자로 변경
swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경
'''
lan = 'python Programming'
print(lan.upper()) # PYTHON PROGRAMMING
print(lan.lower()) # python programming
print(lan.capitalize()) # Python programming
print(lan.swapcase()) # PYTHON pROGRAMMING
print(lan.title()) # Python Programming

'''
문자열 정렬 : 정렬 문자 <,>,^
문자 : 왼쪽 정렬, 숫자 : 오른쪽 정렬
< : 왼쪽 정렬

ljust(자릿수) : 왼쪽 정렬
rjust() : 오른쪽 정렬
center() : 가운데 정렬
'''
string = 'python'
num = 1234
print(string)
print('{:<10}'.format(string)) # 전체 10자리로 해서 왼쪽 정렬 해라
print('{:>10}'.format(string)) # 전체 10자리로 해서 오른쪽 정렬 해라
print(num)