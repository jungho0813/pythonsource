# 파이썬 자료형
# 1. 문자열
# "", '', """ """, ''' '''

# + : 결합
print("Python "+"is fun")

# * : 복제(곱하기)
print("Python"*3)

print("*"*50)
print("내 프로그램")
print("*"*50)

# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)
str1 = "Life is too short"
print(str1[3])

# 슬라이싱 [시작위치 : 끝위치] => 끝 위치 포함하지 않음
print("str1[2:6]",str1[2:6])
print("str1[:6]",str1[:6])
print("str1[:]",str1[:])
print("str1[:-4]",str1[:-4])

# len() : 길이 함수
print("str1 길이", len(str1))

str2 = "20230615Sunny"
# 년도, 날씨를 구별해서 변수에 담기
date = str2[:8]
weather = str2[8:]
print(date,weather)

# date 변수에 담긴 값을 년-월-일
year = date[:4]
month = date[4:6]
day = date[6:]

print(year,month,day,sep="-")

str1 = "대한민국"
for s in str1:
    print(s+ "$",end="")
    
#입력받은 숫자만큼 하트 출력
# 54321
# ♥♥♥♥♥
# ♥♥♥♥
# ♥♥♥
# ♥♥
# ♥
print()
# str1 = input("숫자를 입력해 주세요")
# for i in range(len(str1)):
#     for j in range(int(str1[i])):
#         print("♥",end="")
#     print()

# 문자열 관련 함수
# count
print("\n문자열 관련 함수")
str1 ="hobby"
print("원본 문자열에 포함된 특정 문자 개수 ",str1.count("b"))


# find() : 없는 경우 -1 반환
str1="python is best choice"
print("찾는 문자의 시작 위치 반환",str1.find("b"))
print("찾는 문자의 시작 위치 반환",str1.find("k"))
print("찾는 문자의 시작 위치 반환",str1.find("i"))
