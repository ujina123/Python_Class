'''
literal : 정수, 실수, 문자, 문자열, 논리값
블록(block) : 여러 줄 주석
'''

# 정수 리터럴
a = 10 # 10진수
b = 0b1010 # 2진수 == 10
b2 = 0b1111 # 15
c = 0o61 # 8진수
d = 0x1f2c # 16진수

print(a,b,b2,c,d)

# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234e5

print(f1,f2,f3)

# 문자 리터럴
c1 = 'a'
c2 = 'b'

print(c1,c2)

# 문자여 리터럴
str1 = '이경미'
str2 = 'Hello'
str3 = """여러 줄로 나누어
사용할 수 
있어요. """

print(str1, str2, str3)

# 논리값 리터럴 : True or False
t = True
f = False
print(t,f)

# 특수 리터럴 : None (값이 없는 것)
name = '이유진'
phone = ''
address = None

print(name, phone, address)
print(type(address)) # 데이터의 형태 <class 'NoneType'>