'''
< Variable >

1. reference : 값(객체)이 저장된 메모리의 위치를 가리키는 레퍼런스(reference: 참조)
2. 동적타이핑 (dynamic typing) : 값의 형태에 따라서 고정 되지 않고, 동적으로 자료 유형을 매핑해서 사용 
    type 검사 (자료형이 지정되어 있지 않다.)
3. 변수는 이름을 가지고 있다. 
4. 변수에는 다른 값을 저장할 수 있다. (값 변경 가능)
    그래서 변수라고 부른다. 
5. 변수 선언 필요 없음
    필요한데서 변수 만들어서 값 저장하면 된다. 

< 변수 이름 >
1. 대소문자 구분 : C 언어 개선
2. 영문자, 숫자, 밑줄(_)
3. 중간에 공백 없이
    snake : std_name
    camel : stdName
4. 예약어는 변수명을 사용할 수 없다. 
    import keyword
    keyword.kwlist
    len(keyword.kwlist) == 35

< 변수에 값 저장 : 할당(assign) >
변수 = 값
변수1, 변수2, 변수3 = 값1, 값2, 값3

# 연결 연산자를 숫자와 문자 형태에서 사용하게 되면 type error가 발생

'''

# 화씨 온도 -> 섭씨 온도
fTemp = 80
cTemp = (fTemp-32) * 5/9

print("%.2f"%cTemp)
print("%5.2f"%cTemp)

print(format(cTemp,'.2f'))
print(format(cTemp,'10.2f'))
