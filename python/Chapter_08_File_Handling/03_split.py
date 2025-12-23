# 문자열을 분할해서 문자열 list 만들기 

msg = "123 345 765 12"
result = msg.split(" ")
print(result)

# 문자열을 숫자로 변경하고자 할 때는 int(문자열), float(문자열)
print(result[0] + result[1])
print(int(result[0]) + int(result[1]))
