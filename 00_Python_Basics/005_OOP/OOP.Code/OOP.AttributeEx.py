# 클래스
class Address:
    # 클래스가 소유하는 변수
    num = 0

# Address 클래스의 인스턴스 생성
address = Address()
print(Address.num)
print(address.num)
print("------------")
# 클래스를 이용해서 수정
Address.num = 10
print(Address.num)
print(address.num)
print("------------")
# 인스턴스를 이용해서 수정: 인스턴스 안에 별도로 생성하고 클래스의 속성은 변경하지 않음
address.num = 20
print(Address.num)
print(address.num)
print("------------")