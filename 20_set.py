'''
set : 집합 형태의 자료 구조 (집합 자료형)
1. 중복을 허용하지 않는다. : unhashable tpye
2. 입력 순서와 출력되는 순서가 다를 수 있음
3. 인덱스 사용 불가 : 이미 포함되어 있는 요소를 변경할 수 없음
4. 추가, 삭제 가능
5. 집합 안에 변경 가능한 항목 포함 불가능 : 리스트 포함 불가, 튜플 포함 가능
6. 요소 삭제 가능 : del()
7. set의 연산 (교집합, 합집합, 차집합)
'''

# 1,2.
s4 = {1,3,2,2,5,4,3}
print(s4) # {1, 2, 3, 4, 5}

# 3.
# print(s4[0]) ==> TypeError: 'set' object is not subscriptable

# 4.
# 1개 추가 : add() 메소드 사용
s4.add(10)
print(s4)

# 여러개 추가 : update() 메소드 사용
s4.update([5,6])
print(s4) # {1, 2, 3, 4, 5, 6, 10}

# 요소 삭제
s4.remove(2) # 삭제하려는 요소가 없다면 keyerror가 발생한다. (요소를 key로 간주함)
print(s4) # {1, 3, 4, 5, 6, 10}

s4.discard(1) # 삭제하려는 요소가 없는 경우 에러 없음
print(s4) # {3, 4, 5, 6, 10}

# 데이터 전체 지우기 => 결과 : 빈집합
s4.clear()
print(s4)

# 5.
# s5 = {1,2,[3,4]} ==> TypeError: unhashable type: 'list'
s6 = {1,2,(3,4)}
print(s6)

# 6. Set의 연산
A = {1,2,3}
B = {3,4,5}

# 교집합
C = A & B
print(C)

C = A.intersection(B)
print(C)

# 합집합
C = A | B
print(C)

C = A.union(B)
print(C)

# 차집합
C = A - B
print(C)

C = A.difference(B)
print(C)

D = B - A
print(D)

D = B.difference(A)
print(D)

## 연습문제) 파티에 참석한 사람이 다음과 같을 때 집합 생성하고 그림과 같이 출력
partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "길동", "몽룡"}

all = partyA.union(partyB)
inter = partyA.intersection(partyB)
pA = partyA.difference(partyB)
pB = partyB.difference(partyA)

print(f"파티에 참석한 모든 사람 \n{all}") # {'몽룡', '길동', 'Lee', 'Kim', 'Park'}
print("-"*33)
print(f'2개의 파티에 모두 참석한 사람\n{inter}') # {'Park'}
print('-'*33)
print(f'파티A에만 참석한 사람\n{pA}') # {'Lee', 'Kim'}
print('-'*33)
print(f'파티B에만 참석한 사람\n{pB}') # {'몽룡', '길동'}