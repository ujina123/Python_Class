'''
함수에 리스트 전달
'''

def showNames(names):
    print(names)

nameList = ['홍길동','강감찬','이순신']
showNames(nameList)

'''
함수에 딕셔너리 전달
'''

def showInfo(info):
    print(info)
    for item in info.keys():
        print(item)

info = {'name':'홍길동','age':23, 'phone':'010-1234-1234'}
showInfo(info)