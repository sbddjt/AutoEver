li = [100, 200, 300]

try:
    print(li[4])
except IndexError as e:
    print(e)
else:
    print("예외가 발생하지 않았을 때 처리")
finally:
    print("예외 발생 여부와 상관없이 처리")