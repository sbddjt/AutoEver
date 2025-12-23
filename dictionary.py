# 하나의 데이터를 클래스를 이용해서 만드는 경우
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    __slots__ = ['name', 'age']

# 데이터를 만드는 부분
person1 = Person()
person1.name = "adam"
person1.age = 25

person2 = {"name": "eve", "age": 22}

# 데이터를 출력하는 부분
print(f"이름: {person1.name}, 나이: {person1.age}")

for key in person2:
    print(f"{key} : {person2[key]}", end=" ")
