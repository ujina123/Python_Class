'''
날짜, 시간 형식 데이터 포맷
'''
from datetime import date, datetime,timedelta

print(date.today()) # 현재 날짜
print(datetime.today()) # 연월일, 시간, 1/1000초까지 나타내준다.

today = date.today()
year = date.year
month = today.month
day =  today.day
print(f'{year}년 {month}월 {day}일')

# 현재의 시간
current_time = datetime.now().time()

time = current_time.hour
minute = current_time.minute
second = current_time.second
microsec = current_time.microsecond

# timedelta() : 날짜를 기준으로 재계산 할 수 있다. 
print(today + timedelta(days=-1)) #하루 전 날짜
print(today + timedelta(days=1)) #하루 후 날짜
print(today + timedelta(days=-7)) #일주일 전 날짜
print(today + timedelta(days=7)) #일주일 후 날짜

current_time = datetime.now()
print(current_time + timedelta(hours=-1)) #한시간 전
print(current_time + timedelta(days=1,hours=2)) 

## strftime() 함수 : 날짜 형식을 문자열로 반환
cur_now = datetime.now()
print(cur_now.strftime('%Y-%m-%d %H:%M:%S')) # 2022-01-06 10:07:15
print(cur_now.strftime('%Y-%m-%d %I:%M:%S %p')) # %I : 12시간 %p : 오전 오후  # 2022-01-06 10:07:15 AM

## strptime() 함수 : 문자열을 날짜 형식으로 반환
today = '2020-06-20 17:40:20'
transToday = datetime.strptime(today,'%Y-%m-%d %H:%M:%S') # today 문자열을 다음 형식으로 변환
print(transToday, type(transToday)) # 2020-06-20 17:40:20 <class 'datetime.datetime'>

