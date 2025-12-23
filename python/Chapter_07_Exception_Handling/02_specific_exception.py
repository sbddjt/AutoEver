def ten_div(x : int) -> float:
    try:
        # 예외가 발생하면 except 절로 이동해서 처리
        return 10 / x
    # 잘못된 인덱스를 사용하는 경우에 발생하는 예외만 처리
    except IndexError:
        return 100
    # 0으로 나누는 경우에 발생하는 예외만 처리
    except ZeroDivisionError:
        return 0
    
print(ten_div(10))
print(ten_div(5))
print(ten_div(0))