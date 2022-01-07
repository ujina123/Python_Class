'''
튜플 : tuple
원소 추가, 삭제, 변경 불가능
튜플 생성 : (), tuple()

- 인덱스로 접근해서 변경 불가 : assignment 불가
- 튜플의 요소를 변경 불가 : 리스트로 변환하여 변경 가능
- index() : 요소의 위치
- count() : 일치 항목의 개수
- del() : 튜플 삭제 
'''
t1 = (1,2,3)
print(t1)
print(type(t1))

t2 = 4,5,6
print(t2)
print(type(t2))

t3 = tuple()
print(t3)

t4 = [1,2],[3,4]
print(t4)
print(type(t4[0]))

# 튜플의 요소를 변경 불가 : 리스트로 변환하여 변경 가능
to_list1 = list(t4)
print(to_list1)

t4 = tuple(to_list1)
print(t4)

# 요소의 위치 index(), 
print(t2.index(5)) # 1
# 일치 항목의 개수 count()
print(t2.count(4)) # 1

# 튜플 삭제 : del()
del(t1)
# print(t1) : error(t1 없기 때문에)

## 튜플 사용
print('---튜플 사용 ---')
# 튜플 요소 접근 : indexing

t1 = (10,30,-10,50,100)
print(t1[0] + t1[3]) # 60

# 튜플 범위에 접근 : slicing
print(t1[1:3]) # (30, -10)

# 튜플의 덧셈 및 곱셈 연산 : +, *
t2 = ('a','b','c')
print(t1+t2) # (10, 30, -10, 50, 100, 'a', 'b', 'c')
print(t2*3) # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# 2차원 튜플
tt = ((1,2,3),(4,5,6),(7,8,9))
print(tt) # ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tt[0][-1]) # 3
print(tt[-1]) # (7,8,9)

myTuple = (10,20,30)
myTuple = list(myTuple)
myTuple.append(40)
print(tuple(myTuple)) # (10, 20, 30, 40)

myTuple = (10,20,30)
update = (40,) # 콤마를 사용하면 튜플로 인식 (약속)
myTuple = myTuple + update
print(myTuple) # (10, 20, 30, 40)