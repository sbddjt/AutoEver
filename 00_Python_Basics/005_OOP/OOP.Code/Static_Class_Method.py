class Address:
    auto_increment = 1

    @staticmethod
    def method1(initValue):
	    print("이 메서드로 하는 일은 일반적으로 static 변수의 초기화를 수행합니다.")
        Address.auto_increment = initValue

    @classmethod
    def method2(cls, initValue):
        print("이 메서드로 하는 일은 일반적으로 static 변수의 초기화를 수행합니다.")
        Address.auto_increment = initValue

    def __init__(self, name, phone = "전화번호없음"):
        self.id = Address.auto_increment
        self.name = name
        self.phone = phone
        Address.auto_increment += 1
        print(f"{self.name} 주소록 인스턴스가 생성되었습니다.")

    def __del__(self):
        Address.auto_increment -= 1
        print(f"{self.name} 주소록 인스턴스가 삭제되었습니다.")

    # id를 위한 접근자 메서드
    def get_id(self):
        return self.id

    # name을 위한 접근자 메서드
    def get_name(self):
        return self.name
    
    # phone을 위한 접근자 메서드
    def get_phone(self):
        return self.phone

address = Address(name = "홍길동", phone ="010-1234-5678")
print(address.get_id())
address = None

address2 = Address(name = "김철수", phone = "010-9876-5432")
print(address2.get_id())

address3 = Address(name = "이영희")
print(address3.get_id())
