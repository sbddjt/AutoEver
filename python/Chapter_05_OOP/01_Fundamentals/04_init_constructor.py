class Address:
    auto_increment = 1
    
    def __init__(self, name, phone = "전화번호없음"):
        self.id = Address.auto_increment
        self.name = name
        self.phone = phone
        Address.auto_increment += 1

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

address2 = Address(name = "김철수", phone = "010-9876-5432")
print(address2.get_id())

address3 = Address(name = "이영희")
print(address3.get_id())
