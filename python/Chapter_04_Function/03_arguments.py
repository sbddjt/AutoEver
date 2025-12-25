# 기본 함수 정의
def sub(first : int, second : int) -> int:
    result = first - second
    return result

# 1. Keyword Arguments
print(sub(100, 200))                  # 위치 기반
print(sub(first = 100, second = 200)) # 키워드 기반
print(sub(second = 200, first = 100)) # 순서 변경


# 2. Default Parameter Value
def sub_default(first : int, second : int = 0) -> int:
    result = first - second
    return result

print(sub_default(first = 100, second = 200))
print(sub_default(first = 100))


# 3. Parameter Unpacking
# List Unpacking (*)
print(sub(*[100,70]))

# Dict Unpacking (**)
print(sub(**{"first" : 100, "second" : 70}))
