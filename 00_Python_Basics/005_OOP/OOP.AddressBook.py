# 클래스
class Address:
    # 인스턴스가 호출가능한 메서드
    def printAddress(self):
        print("인스턴스 메서드 만들기 연습")

# Address 클래스의 인스턴스 생성
myAddress = Address()

# 바운드 호출: 인스턴스 이름으로 호출
myAddress.printAddress()

# 언바운드 호출: 클래스 이름으로 호출, 인스턴스를 첫 번째 매개변수로 전달
Address.printAddress(myAddress)