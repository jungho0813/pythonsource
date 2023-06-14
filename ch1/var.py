# 변수 : 타입 없음, 값을 삽입 시 타입 결정
# 타입 : 숫자형 - int, float
#        문자형 - str,
#        불 - bool
#        여러가지 데이터 한꺼번에 처리 - list, set, dict, tuple

# 문자열 : "", '', """한글""", '''한글'''

str1 = "Life is too short, You need Python"
str2 = "Life is too short, You need Python"
str3 = """Life is too short, You need Python"""
str4 = """Life is too short, You need Python"""

print(str1)
print(str2)
print(str3)
print(str4)

print()
num1 = num2 = 10
print(num1, num2)
num1, num2 = 10, 15
print(num1, num2)
num1, num2 = num2, num1
print(num1, num2)

num1 = "한글"
print(num1)

print(num1 + str(num2))

a, b = 5, 4
print("a + b = %d" % (a + b))
print("a - b = %d" % (a - b))
print("a * b = %d" % (a * b))
print("a / b = %f" % (a / b))
print("a // b = %f" % (a // b))
print("a % b = ", (a % b))
print("a ** b = %d" % (a**b))

# type() : 변수 타입 확인
# str() : 문자열 변환 ,int() : 숫자로 변환, float() : 실수로 변환, bool() : boolean 변환
print(str(3.5), type(str(3.5)))
print(int(True), type(int(True)))
print(bool(0.1), type(bool(0.1)))

money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = 7777

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10


print("500원 : {}개".format(c500))
print("100원 : {}개".format(c100))
print("50원 : {}개".format(c50))
print("10원 : {}개".format(c10))
print("나머지 돈 : {}원".format(money))

# ||, &&, ! (X) ==> or , and, not
a, b, c = 100, 60, 15
print("and : ", a > b and a > c)
print("or : ", a > b or a > c)
print("not : ", not (a > b))
