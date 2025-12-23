data = [23, 25, 18, 20, 30]

# data의 각 요소에 2를 곱해서 새로운 list 생성

# 기본적인 방법
result = []
for i in data:
    result.append(i*2)
print(result)

# list comprehension 방법
result = [i*2 for i in data if i > 20]
print(result)