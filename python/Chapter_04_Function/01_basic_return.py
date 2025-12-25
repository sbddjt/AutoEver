# 기본 형식 및 Type Hinting
def interAddWithInteger(first: int, second: int) -> int:
    """정수 2개를 더해서 리턴하는 함수"""
    result = first + second
    return result

# 호출
k = interAddWithInteger(20, 30)
print(f"Result: {k}")


# 튜플 리턴 (여러 데이터 리턴)
def tupleReturn(first : int, second : int) -> tuple: # 반환되는 자료형을 되도록 쓰자
    result1 = first + second
    result2 = first - second
    return (result1, result2)

print(tupleReturn(100, 200))
