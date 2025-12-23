class Address:
    auto_increment = 1

    __slots__ = ['__id', '__name', '__phone']

    def __init__(self, name, phone="전화번호없음"):
        self.__id = Address.auto_increment
        self.__name = name
        self.__phone = phone
        Address.auto_increment += 1
        print(f"✨ {self.name} 주소록 인스턴스가 생성되었습니다. (ID: {self.id})")

    def __del__(self):
        Address.auto_increment -= 1
        print(f"🗑️ {self.name} 주소록 인스턴스가 삭제되었습니다. (현재 카운트: {Address.auto_increment})")

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id 

    id = property(fget = getId)

    def getName(self):
        return self.__name
    def setName(self, name):
        print("name의 setter 호출됨!")
        if len(self.__name) >= 3:
            print("이름이 너무 깁니다.")
            return
        self.__name = name
    
    name = property(fget = getName, fset = setName)

    def getPhone(self):
        return self.__phone
    def setPhone(self, phone):
        self.__phone = phone

    phone = property(fget = getPhone, fset = setPhone)

# --- 테스트 코드 ---
address = Address("홍길동","010-1234-5678")
address.name = "adam" # 이름 조건에 안 맞아서 setter에서 걸림
print(address.name)