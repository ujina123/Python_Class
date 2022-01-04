# 입력 내용이 긴 경우 여러 줄에 작성해야 할 때
sum = 1 + 2 + 3 + 4 + \
    5 + 6 + 7 + 8

sum = (1 + 2 + 3 + 4 + 
    5 + 6 + 7 + 8)

# 1줄로 인식 
print("긴문장으로 표현하지만"
      "결과는 한 줄로"
      "표시된다.")

# 여러줄로 인식
print("긴 문장으로 표현 \n"
      "여러줄로 \n"
      "표시된다.\n")

'''
< escape character >
문법적인 의미에서 벗어나서 그대로 쓰고 싶을 때 '\' 사용
\n : 줄바꿈
\t : tab
\' : '
\" : "
\\ : \

< 특수(escape)문자 의미 제거 : r >
print(r'c:\path')

< 2개 명령어(문장)를 한 줄에 입력 >
print(sum1) ; print(sum2)
'''

print('apple \nbanana \nmelon')

print('apple')
print('banana')
print('melon')

# apple -> banana -> melon
print('apple',end=' -> ')
print('banana',end=' -> ')
print('melon')