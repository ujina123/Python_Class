'''
break & continue

break는 for와 while문법에서 제어흐름을 중단하고 빠져 나오지만, 
continue는 제어흐름(반복)을 유지한 상태에서 코드의 실행만 건너뛰는 역할을 한다.
'''
for i in range(10):
    if i % 2 == 0:
        continue # 다음 반복을 수행하게 한다.
    print(i)

for i in range(10):
    if i % 2 == 0:
        break
    print(i)

print("-"*30)

for i in range(10):
    if i % 2 == 1:
        continue
    print(i)

i = 1
while i < 10:
    if i % 2 == 0:
        break
    print(i)
    i += 1

print('-'*30)

i = 1
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    i += 1