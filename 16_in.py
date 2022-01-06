'''
< in / not in >
문자열 내에 특정한 문자열이 포함되어 있는지 확인하는 명령어
결과 ) True, False

< 문자열 구성 파악 >
isalpha() : 문자 여부 결과 반환 (True, False)
isdigit() : 숫자인지 결과 반환
issoace() : 하나의 문자에 대하여 공백 여부 반환
isalnum() : 문자 또는 숫자인지 확인
islower() : 소문자 여부
isupper() : 대문자 여부
'''

string = '내 이름은 k 이고, 나이는 12살 입니다.'
str_split = string.split()
for str in str_split:
    if str.isdigit(): # 숫자인지에 대한 결과 반환
        print('숫자')