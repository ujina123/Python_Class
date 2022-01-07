'''
딕셔너리(dictionary) : 키와 값의 쌍으로 이루어진 데이터
{키1:값1, 키2:값2, ... }

딕셔너리 생성 :  {} or dict()
'''

students = {1:'최선', 2:'홍길동', 3:'강감찬'}
print(students, type(students)) # {1: '최선', 2: '홍길동', 3: '강감찬'} <class 'dict'>

prof = {} # 빈 딕셔너리 생성
prof[1] = '이순신'
prof[2] = '홍길동'
print(prof) # {1: '이순신', 2: '홍길동'}

print(students[1]) # key로 value를 찾는다. : 최선

member = {'name':'홍길동', 'phone':'010-123-1234'}
print(member) # {'name': '홍길동', 'phone': '010-123-1234'}
print(member['name']) # 홍길동

# 같은 key값이 들어가면 기존의 key의 value는 지워지고 새로운 value가 출력된다.
member1 = {'name':'홍길동','phone':'010-1234-1234','name':'이순신'}
print(member1) # {'name': '이순신', 'phone': '010-1234-1234'}

naver = {'name':'naver',
         'url':'www.naver.com',
         'id':'lee'}
google = {'name':'google',
         'url':'www.google.com',
         'id':'kmlee'}
daum = {'name':'daum',
         'url':'www.daum.com',
         'id':'kmlee'}

print(naver['name']) # naver
naver['id'] = 'idValue'
print(naver['name']) # naver

# keys(), values(), items()
print(naver.keys()) # dict_keys(['name', 'url', 'id'])
print(naver.values()) # dict_values(['naver', 'www.naver.com', 'idValue'])
print(naver.items()) # dict_items([('name', 'naver'), ('url', 'www.naver.com'), ('id', 'idValue')])
for key in naver.keys():
    print(key)

for value in naver.values():
    print(value)

for item in naver.items():
    print(item)

# key 로 value 찾기
print(naver['name']) # naver
print(naver.get('name')) # naver

print(naver.get('passwd','없음')) # 없음

key = 'passwd'
if naver.get(key) is None:
    print(key + '에 대한 값이 없습니다.')
# passwd에 대한 값이 없습니다.

## 예제 문제. 음식 정보를 딕셔너리로 생성, 음식 정보들은 리스트로 구성
data1 = {'name':'버섯불고기',
         'class':'한식',
         'type':'불고기',
         'ingr':['소고기','버섯','양파','간장']}

data2 = {'name':'카레덮밥',
         'class':'양식',
         'type':'덮밥',
         'ingr':['카레','감자','양파','당근']}

datum = [data1,data2]
print(datum)

# 음식정보 출력하기
i=1
for data in datum:
    print('음식'+str(i))
    for d in data.keys():
        print(d ,':', data.get(d) )
    i +=1
    print('--------------')
