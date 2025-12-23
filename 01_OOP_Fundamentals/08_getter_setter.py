# 클래스
class Address:
    # 클래스가 소유하는 변수
    num = 0

    def getNum(self):
        return self.num

    def setNum(self, num1):
        self.num = num1
# Address 클래스의 인스턴스 생성
address = Address()
address.setNum(10)
print(address.getNum())