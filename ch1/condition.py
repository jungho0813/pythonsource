# 조건문
# if, if~else, if~elif,else
if True :
    print("True")

a = 100

if a < 100 :
    print ("a는 100보다 작다")
print("조건문에서 하나의 블럭 개념은 들여쓰기로 구분")

if 100 < a <= 200:
    print("a는 100보다 크고 200보다 작거나 같다")

a,b,c = 12,6,18
max = a
if max < b:
    max = b
if max < c:
    max = c
print("가장 큰 수 {}".format(max))

a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 크다")

# 숫자 입력 받은 후 홀,짝 구분후 출력
#num1 = int(input("숫자 입력 : "))
#if num1 % 2 == 0:
#    print("짝")
#else:
#    print("홀")

import datetime

now = datetime.datetime.now()
print(now)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

if now.hour < 12:
    print("오전")
else:
    print("오후")

# 삼항연산자 now.hour < 12 ? "오전":"오후"(X)
# 참일때 실행 구문 if 조건 else 거짓일때 실행 구문

print("오전"if now.hour < 12 else "오후")

# 다중조건 if ~ elif ~ else

num = 90
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
else :
    print("C")

# age, height 변수 선언, 27, 180 값 담기
# 나이가 20세 이상 지원 가능
#       키가 170 이상이면 "A지망 지원 가능"출력
#       키가 160 이상이면 "B지망 지원 가능"출력

age, height = 27, 180

if age >=20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else :
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

# 계산기 : 두 개의 수 입력, 연산자(+,-,*,/,//,%,**) 입력
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
t = input("연산자 : ")

if t == '+' :
    print(num1 + num2)
elif t == '-' :
    print(num1 - num2)
elif t == '*' :
    print(num1 * num2)
elif t == '/' :
    print(num1 / num2)
elif t == '//' :
    print(num1 // num2)
elif t == '%' :
    print(num1 % num2)
elif t == '**' :
    print(num1 ** num2)

