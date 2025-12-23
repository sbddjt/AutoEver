# 기본적인 예외 처리 : 예외가 발생하면 0이 리턴되도록 작성
def ten_div(x : int) -> float:
    try:
        # 예외가 발생하면 except 절로 이동해서 처리
        return 10 / x
    except:
        return 0

print(ten_div(2))
# 정수를 대입했으므로 문법적으로 오류는 없는데 실행하다가 0으로 나눌 수 없어서 예외가 발생
print(ten_div(0))
print(ten_div(5))