# 파이썬 자료형
# 2. 리스트
# []

# 리스트 생성 - 데이터는 아무거나 가능
list1 = []
list2 = ["a", 1, 3.15, True]
print(list1)
print(list2)
list3 = ["a",1, 3.15, True, ["b",35,45]]
print(list3)


# 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1])

print(list3[-1])
print(list3[-1][1])

# 리스트 슬라이싱
print(list2[0:2])
print(list3[:-1])
print(list3[4:])
print(list3[4])
print(list3[4][:2])

list4 = [1,2,["a","b",["Life","is"]]]
print(list4[2][2][1])

