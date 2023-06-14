# 반복문
# while, for

i = 1
while i < 11:
    print(i, end=" ")
    i += 1

print()

# 짝수만 출력
i = 2
while i < 101:
    print (i, end =" ")
    i += 2

print()

# in
print("in 기호")
print("y" in "python")

# range(시작값, 종료값, 증감값) : 범위 지정
print(range(5))
print(list(range(1,5)))
print(list(range(0,10,2)))

# for
for i in range(10):
    print(i)