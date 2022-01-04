'''
while

정해진 조건에 따라 반복문 수행

초기값
while 조건 = True:
    반복문장1
    반복문장2
    ...
    초기값 증감 (무한루프를 방지하기 위해 while문 안에 조건이 False인 것도 넣어줘야함!)
'''


# 1부터 10까지 출력
print('-- for문 사용 --')
for i in range(1,11):
    print(i, end=' ')

print('\n-- while문 사용 --')

i = 1
while i <= 10 :
    print(i,end = ' ')
    i += 1

print('\n-- 1에서 10까지 더하기 --')
i = 1
sumN = 0
while i <= 10 :
    sumN += i
    i += 1
print(sumN)

# stop까지 정수를 입력 받아 양수, 음수, 0의 개수 출력
num = input('숫자 입력 : ') # 최소 한번의 입력
cnt = 0
while num != 'stop':
    num = input('숫자 입력 : ')
    cnt += 1
    if num == 'stop':
        print(num)
print('숫자 개수:',cnt)

# 숫자 7을 입력할 때까지 계속 입력하기
# 7이 입력되면 프로그램 종료
state = True
while state:
    num = int(input("숫자 입력: "))
    if num == 7:
        print(num + "입력!종료")
        state = False

# while & break : 무한루프 이용
# 알파벳 'q'가 입력되면 종료

while True:
    s = input("입력 : ")
    if s == 'q':
       break
print("input! exit!")