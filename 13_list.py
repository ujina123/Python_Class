'''
list(리스트) : 집합적 자료형이다. (여러 개의 원소를 가지는 데이터)
1. 가변적 : 삽입, 삭제, 변경 가능
2. 다양한 형식의 데이터를 가질 수 있다. : 숫자, 문자열, 논리
3. 리스트 : []
'''
# 리스트 생성
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


'''
리스트의 길이 : len(리스트 이름)
len() : list or string의 길이를 알려주는 함수
리스트 인덱싱 : 리스트의 인덱스를 이용하여 접근 : 리스트명[인덱스 번호]
'''
print('문자열의 길이: ',len(list4))
for i in range(0,len(list4)):
    print(list4[i], end = ' : ')
    print(type(list4[i]))


# 리스트의 각각의 값은 변수에 저장
nums = [1,2,3]
a,b,c = nums
print(a,b,c)

'''
list indexing
인덱싱의 결과는 해당하는 값의 요소 반환
[] : 리스트에서 인덱스 연산자를 통하여 요소를 참조하거나 또는 접근하는 것
'''