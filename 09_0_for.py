'''
정해진 횟수만큼 반복
for 변수 in 리스트 또는 범위:
    반복문장1
    반복문장2
    ...

range(시작값, 끝값+1)
range(끝값+1) : 0~끝값
range(시작값, 끝값+1, 간격) : 시작값부터 끝값까지 간격으로 출력
'''

## for에서 리스트를 이용
## 문제 : 학생 성적 리스트 score = [70,90,100,50,85]
score = [70,90,100,50,85]
for i in range(len(score)):
    if score[i] >= 60 :
        res = '합격'
    else :
        res = '불합격'
    print("%d 번째 학생 %s" %(i+1,res))

## 문제 : 숫자 10개를 입력 받아서 양, 음, 0의 개수 출력
posi,nega,zero= 0,0,0
for i in range(0,10):
    num = int(input("숫자%d 입력 : " %(i+1)))
    if num > 0 :
        posi += 1
    elif num == 0 :
        zero += 1
    else:
        nega +=1
print("양의 개수 : %d \n음의 개수 : %d \n0의 개수 : %d" %(posi,nega,zero))

## 문제 : 리스트에 있는 이름인지 확인
# 방법1)
names = ['베토벤','홍길동','변학도','아쿠아맨']
search_name = input("찾고 싶은 이름을 입력하세요 : ")
if search_name not in names:
    print("%s님은 명단에 존재하지 않습니다." %search_name)
else : print("%s님은 명단에 존재합니다." %search_name)

# 방법2)
for name in names :
    if search_name == name:
        print("%s님은 명단에 존재합니다." % search_name)
        find = True
        break
    else:
        print("%s님은 명단에 존재하지 않습니다." %search_name)

# 방법3)
for name in names :
    if search_name == name:
        find = True
        break
    else:
        find = False
if find :
    print("명단에 있어요")
else:
    print("명단에 없어요")

## 중첨 for문
## 구구단 전체 출력
for i in range(2,10):
    for j in range(1,10):
        print('%d * %d = %d' % (i,j,(i*j)),end=" ")
    print(" ")

for y in range(3):
    for x in range(5):
        print(x, end=' ')
    print()
'''    
1 2 3 4 
5 6 7 8 
9 10 11 12
'''
n=1
for y in range(3):
    for x in range(4):
        print(x+n, end = ' ')
    print()
    n += 4
