li = [100, 200, 300]

try:
    print(li[4])

# 예외가 발생했을 때 예외 내용을 e에 전달
except IndexError as e:
    print(e)
except Exception:
    print("나머지 예외 처리")