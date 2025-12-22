class Address:
    auto_increment = 1

    # id를 위한 접근자 메서드
    def get_id(self):
        return self.id
    
    def set_id(self):
        self.id = Address.auto_increment
        Address.auto_increment += 1

    # name을 위한 접근자 메서드
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    # phone을 위한 접근자 메서드
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone

address = Address()
address.set_id()
address.set_name("홍길동")
address.set_phone("010-1234-5678")

print(address.get_id())

address2 = Address()
address2.set_id()
address2.set_name("김철수")
address2.set_phone("010-9876-5432") 

print(address2.get_id())
