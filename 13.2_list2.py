'''
1. 리스트 요소 삽입 
- insert(i,x) : 리스트의 원하는 위치에 값을 삽입
    i : 인덱스, x : 삽입하려는 값

2. 리스트 요소 제거
- remove(값) : 지정한 값을 제거
    > 동일한 값은 한번에 제거 할 수 없다. 제일 앞쪽에 있는 요소만 지운다.
- pop() : 마지막 요소의 값을 제거
- pop(indx) : indx 위치의 요소값을 제거 

3. 리스트 확장
- extend()

4. 리스트 정렬 
list.sort([key=str.lower, reverse = True]) : list 정렬
list.reverse() : 원래 리스트의 순서를 인덱스 역순으로 변경
sorted(리스트) : 원본은 수정하지 않고 새롭게 리스트 정렬하는 함수

5. 리스트 안에 원하는 원소의 위치값 반환
- index(value)
- 찾고나 하는 원소가 없는 경우 error 발생

6. 리스트 일치 검사 : ==, !=, >, < 등
'''

##1. insert()
x = ['apple','banana','coconut','melon']
print(x) # ['apple', 'banana', 'coconut', 'melon']
x.insert(1,'watermelon')
print(x) # ['apple', 'watermelon', 'banana', 'coconut', 'melon']

##2. 요소 제거 예제
x = ['apple','banana','banana','coconut','melon','melon']
x.remove('melon')
print(x) # ['apple', 'banana', 'banana', 'coconut', 'melon']

# 바나나 싹 다 지우기
n = x.count('banana')
print(n) # 2
for i in range(n):
    x.remove('banana')
print(x) # ['apple', 'coconut', 'melon']


y = [1,3,5,1,10]
last = y.pop() # 맨 마지막 요소의 값을 가지고 온다. 다른 변수에 저장이 가능하다.
print('y 값 변경 확인 : ',y  ,'\n마지막 값 : ',last)  # y 값 변경 확인 :  [1, 3, 5, 1] \n 마지막 값 :  10

y.append(-10)
print(y) # [1, 3, 5, 1, -10]
rm = y.pop(3)
print('y 값 변경 확인 : ',y  ,'\n마지막 값 : ',rm) # y 값 변경 확인 :  [1, 3, 5, -10] \n 마지막 값 :  1

# y.remove(0)
y[3] = 'list'
print(y) # [1, 3, 5, 'list']

##3. 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)

a.append(9)
print(a)
a.append([-1,10])
print(a)

a.insert(3,[1,2])
print(a)

##4. 리스트 정렬
scores = [90,78,81,64,99]
print('정렬 전 : ',scores) # 정렬 전 :  [90, 78, 81, 64, 99]
scores.sort() 
print('정렬 후 : ',scores) # 정렬 후 :  [64, 78, 81, 90, 99]

scores = [90,78,81,64,99]
scores.sort(reverse=True) # 역순 정렬, 디폴트 값 : reverse = False
print('역순 정렬 : ',scores) # 역순 정렬 :  [99, 90, 81, 78, 64]

scores = [90,78,81,64,99]
scores.reverse()
print('reverse() 적용 후 : ', scores) # reverse() 적용 후 :  [99, 64, 81, 78, 90]

scores = [90,78,81,64,99]
result = sorted(scores)
print(result) # [64, 78, 81, 90, 99]
print(scores) # [90, 78, 81, 64, 99]

# .sort(key=) : 문자코드 순서대로 정렬이 된다. (대문자 -> 소문자)
chr = ['b','A','e','C']
print(chr) # ['b', 'A', 'e', 'C']

chr.sort() 
print(chr) # ['A', 'C', 'b', 'e']

chr.sort(reverse=True)
print(chr) # ['e', 'b', 'C', 'A']

# key = str.lower : 대소문자 구별 없이 알파벳 순으로 정렬
chr.sort(key=str.lower)
print(chr) # ['A', 'b', 'C', 'e']

chr.sort(key=str.lower, reverse=True) # 역순
print(chr) # ['e', 'C', 'b', 'A']

## 5. index(value)
x = ['melon','banana','Coconut','apple']
idx = x.index('Coconut')
print(idx)

