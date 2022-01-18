# * : 변수 앞에 붙은 경우 *args, **kwagrs => 언패킹(unpacking)

def asterisk_test(a, *args):
    print(a,args)
    print(type(args))

def asterisk_test2(a, *args):
    print(a,*args)
    print(type(args))

asterisk_test(1,2,3,4,5)
# 1 (2, 3, 4, 5)
# <class 'tuple'>
asterisk_test2(1,2,3,4,5)
# 1 2 3 4 5
# <class 'tuple'>

a,b,c = [1,2,3]
# a,b,c = ([1,2,3],[1,2,3],[1,2,3],[1,2,3]) # ValueError: too many values to unpack (expected 3)
print(a,b,c)
data = ([1,2,3],[4,5,6],[7,8,9])
print(*data) # [1, 2, 3] [4, 5, 6] [7, 8, 9]

def asterisk_test3(a, **args):
    print(a,args)
    print(type(args))

asterisk_test3(1,b=2,c=3,d=4,e=5)
# 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5}
# <class 'dict'>

data2 = {'b': 2, 'c': 3, 'd': 4, 'e': 5}
asterisk_test3(1,**data2)
# 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5}
# <class 'dict'>