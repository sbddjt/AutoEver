# 1. 스칼라 데이터 (Immutable - Call by Value 성격)
def callByValue(a : int) -> None:
    print("a: ", a)
    a = a + 1
    print("a: ", a)

x = 10
callByValue(x)
print("x: ", x)


# 2. 벡터 데이터 (Mutable - Call by Reference 성격)
def callByReference(li : list) -> None:
    print("li: ", li)
    li[0] = li[0] + 1
    print("li: ", li)

l = [10, 20]
callByReference(l)
print("l: ", l)
