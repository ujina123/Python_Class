'''
내장함수 (built-in function)
1. python에 이미 만들어져 내장 되어 있는 함수들
2. 별도의 모듈을 import 하지 않고 사용 가능

- 함수의 형식과 목적에 따라 호출해서 사용
print(), input(), id(), type(), sum(), int() ...

- 특정 객체를 통해 사용가능한 함수 (메소드 method)
list.index() .append() .insert() .count() .remove() ...
str.index() .find() .sort() .reverse() ...

참고사이트 : https://docs.python.org/ko/3/library/functions.html

1) abs() : 절대값 계산
2) all() : 모든 요소가 참이면 True(0), 하나라도 거짓이면 False(1)
   iterable(반복 가능한 자료형) : 리스트, 튜플, 딕셔너리, 집합
   for 반복문을 이용해서 사용
3) any() : 하나라도 참이면 True
4) bool() : 부울 값으로 변환 True, False
5) chr() : 아스키코드(AScII)값에 해당하는 문자 변환
6) ord() : 문자에 대한 SCILL코드 값으로 변경
7) divmod(a,b) : a를 b로 나눈 목과 나머지 반환
8) enumerate() : 시퀀스를 인덱스를 포함해서 enumerate 객체로 반환
                 인덱스 문자 객체와 같이 보고 싶을 때
                 시퀀스 : range(0), 문자열, 리스트, 튜플
9) eval(표현식) : 표현식의 연산 결과 반환
10) filter(function, interable) : interable자료의 요소들을 function으로 거르다(걸러낸다.)
11) pow(x,y) : x의 y
12) range([start,] stop [,step]) : 지정한 범위의 값을 반복가능한 객체로 반환
13) map() : 리스트나 튜플, 문자열 등 반복 가능한 구조의 요소별로 지정된 함수를 적용하여 처리
            원본은 변경하지 않고, list , tuple 형태로 반환
            list(map(함수, 리스트))
            list(map(함수, 튜플))
'''

# 문제, 실수형 요소를 갖는 리스트를 정수형 요소리스트로 변환
# map을 이용하는 경우
# for를 이용하는 경우

number1 = [3.5,3.4,2.0,4.6]
# for문 사용
def to_int(num_list):
    for num in range(len(num_list)):
        num_list[num] = int(num_list[num])
    print(num_list)
to_int(number1) # [3, 3, 2, 4]

# map 사용
print(list(map(lambda num: int(num),number1))) # [3, 3, 2, 4]
print(list(map(int,number1))) # [3, 3, 2, 4]

# zip(*iterabel) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환

print(zip([1,2,3],[4,5,6])) # <zip object at 0x105030180>
print(list(zip([1,2,3],[4,5,6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

keys = ['apple','melon','banana']
vals = [250,300,400]

print(list(zip(keys,vals))) # [('apple', 250), ('melon', 300), ('banana', 400)]
print(dict(zip(keys,vals))) # {'apple': 250, 'melon': 300, 'banana': 400}


