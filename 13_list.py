'''
< list(리스트) >
- 집합적 자료형이다. (여러 개의 원소를 가지는 데이터)
1. 가변적 : 삽입, 삭제, 변경 가능
2. 다양한 형식의 데이터를 가질 수 있다. : 숫자, 문자열, 논리
3. 리스트 : []

< 리스트의 길이 >
- len(리스트 이름)
len() : list or string의 길이를 알려주는 함수
리스트 인덱싱 : 리스트의 인덱스를 이용하여 접근 : 리스트명[인덱스 번호]

< list indexing >
인덱싱의 결과는 해당하는 값의 요소 반환
[] : 리스트에서 인덱스 연산자를 통하여 요소를 참조하거나 또는 접근하는 것

< 리스트의 슬라이싱 (slicing) >
- 슬라이싱 연산 결과는 리스트 반환
- [start : end] : start에서 end-1 요소까지 선택 

리스트[:n] : 처음부터 n-1 요소까지 선택
리스트[start:] : start부터 마지막 요소까지 선택
리스트[:] : 모든 요소 (복사)
리스트[:-1] : 처음부터 마지막에서 두번째 요소까지 선택
리스트[-1:] : 마지막 요소만 선택
리스트[n:] : n부터 마지막 요소까지 선택

< 리스트 연산 >
1. 리스트 합치기 : +
2. 리스트 곱하기 : * (반복)
3. 리스트 내용 변경

< 리스트 복사 >
1. 얕은 복사 (shallow copy) : 실제 리스트가 복사되지 않고 참조값(주소)만 복사 된다. 
2. 깊은 복사 (deep copy) : 실제 리스트 원본 복사본을 새로 생성하여 반환
    list()함수 또는 deepcopy()함수 사용

< main method of list >
함수 : 함수이름()
      함수이름()으로만 호출해서 사용한다.
      ex) input(), print(), len(), del() : 내장함수
      사용자 정의 함수

      list() : 리스트를 만드는 생성자함수
      len() : 리스트 길이 /개수 (리스트 길이 반환, 원소의 개수)

메소드 : 메소드이름()
       class의 member인 객체를 통해서 사용
       ex) string객체이름.find()

      .count() : 리스트 내의 특정한 요소의 개수 세기
      .append() : 리스트의 맨 뒤에 추가 (빈 리스트를 생성 한 후, 새로운 데이터를 추가할 때 주로 사용)
      .insert(삽입하고자 하는 위치, 삽입하려는 값) : 특정 위치에 값을 삽입

'''

## 리스트 생성
list1 =[] # 빈 리스트 생성
print(list1, type(list1))

list2 = list() # 리스트 함수를 사용하여 빈 리스트 생성
print(list2, type(list2))

list3 = [1,2,3] # 초기에 값이 들어가 있는 리스트
print(list3)

list4 = [1,3.5,[10,20,30],'apple',True]
print(list4)

for l in list4:
    print(f'{l} : {type(l)}')


## 리스트 길이 len()
print('문자열의 길이: ',len(list4))
for i in range(0,len(list4)):
    print(list4[i], end = ' : ')
    print(type(list4[i]))


# 리스트의 각각의 값은 변수에 저장
nums = [1,2,3]
a,b,c = nums
print(a,b,c)


## list indexing
a = [1,'apple',3,5,[10,20,30],True]

print(a[0]) # 첫번째 요소
print(a[-1]) # 마지막 요소
print(a[-5]) # 첫번째 요소
print(a[3]) # 세번째 요소
print(a[4][-1]) # 네번째 요소의 마지막 요소 (2차원일 경우)

b = ['apple','banana','melon']
c = [a,b]
print(c) # [[1,'apple',3,5,[10,20,30],True],['apple','banana','melon']]
print(c[0][4][-1]) # 30 (3차원 리스트)


## 리스트 연산
fruits = ['apple','banana','melon']
a = [1,'apple',3.5,[10,20,30],True]

b = fruits + a
print(b)  # ['apple', 'banana', 'melon', 1, 'apple', 3.5, [10, 20, 30], True]

c = fruits * 3
print(c) # ['apple', 'banana', 'melon', 'apple', 'banana', 'melon', 'apple', 'banana', 'melon']

a[3] = 'melon'
print(a)
a[1:3] = [10,11,12]
print(a)

a[0] = [-1,-4]
print(a)


## 리스트 복사
# 얕은 복사
print("-"* 5, 'shallow copy', '-'*5)
a = [1,2,3,4]
b = a
print(a) # [1, 2, 3, 4]
print(id(a)) # 4366151744
print(b) # [1, 2, 3, 4]
print(id(b))  # 4366151744

a[-1] = 100
print(a) # [1, 2, 3, 100]
print(b) # [1, 2, 3, 100]
b[0] = 0.5
print(a) # [0.5, 2, 3, 100]
print(b) # [0.5, 2, 3, 100]

# 깊은 복사
print("-"* 5, 'deep copy', '-'*5)
c = [1,2,3,4]
d = list(c)
print(c) # [1, 2, 3, 4]
print(id(c)) # 4366152320
print(d) # [1, 2, 3, 4]
print(id(d)) # 4366152384
d[0] = 'apple'
print(c)
print(d)

import copy
d = ['a','b','c']
e = copy.deepcopy(d)

e[0] = 1
print(d)
print(e)

