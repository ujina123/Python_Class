'''
< 문자열 >
str() : 문자열로 변환해주는 함수

문자열에서 사용 되는 연산자 : +, *
+ : 문자열과 문자열을 연결해주는 연산자 -> 하나의 문자열로 합치는 연산
* : 문자열을 곱하는 수만큼 반복해서 생성됨

< 문자열에서 사용되는 함수(메소드)들 >
1. len() : 문자열 길이 반환
2. .count() : 문자열 내에 들어 있는 특정 문자(열)의 개수 반환(메소드)
3. .find(찾을문자[,start[,end]]) : 시작 위치 인덱스 반환, 없으면 -1 반환
4. .index(찾을문자[,start[,end]]) : 문자열 내에서 특정문자열의 시작 위치를 반환, 찾는 문자열이 없으면 에러를 반환

< 문자열 분리 >
split() : 구분자(공백, 세미콜론, 콜론, 콤마, ..)를 기준으로 문자열 나눔 
결과 : 리스트로 반환

< 문자열 정렬 : 정렬 문자 <, >, ^ >
문자 : 왼쪽 정렬
숫자 : 오른쪽 정렬
< : 왼쪽 정렬
ljust(자릿수) : 왼쪽 정렬
rjust() : 오른쪽 정렬
center() : 가운데 정렬

'''

## 문자열에서 사용되는 함수(메소드)들
# .find()
crawling = 'Data crawling is fun'
print(crawling.find('is')) # 14
print(crawling.find('parsing')) # 찾는 문자열이 없는 경우 -1 반환
print(crawling.find('is',15)) # -1
print(crawling.find('is',5,10)) # 인덱스 5부터 10 사이에서 is가 있는지 찾아라

# .index()
print(crawling.index('is')) # 찾으면 인덱스 반환
print(crawling.index('parsing')) # 찾는 문자열이 없는 경우 에러

## ex1, 도시명을 입력하고 해당 도시가 있는지 유무를 출력하기
cities = '인천 대구 대전 부산 울산 청주 춘천'
c = input("도시명 입력 : ")

# 방법1. in 사용
if c in cities:
    print("해당 도시가 존재")
else :
    print("해당 도시가 존재하지 않음")

# 방법2. index()
try:
    cities.index(c)
    print("해당 도시가 존재")
except:
    print("해당 도시가 존재하지 않음")

# 방법3. .find() 사용
if cities.find() != -1:
    print("정답")
else:
    print("오답")
