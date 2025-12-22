class Address:
    auto_increment = 1
    __slots__ = ['__id', '__name', '__phone']

    def __init__(self, name, phone="전화번호없음"):
        self.__id = Address.auto_increment
        # setter를 호출하기 위해 self.name 사용
        self.name = name 
        self.phone = phone
        Address.auto_increment += 1
        print(f"✨ {self.name} 주소록 인스턴스가 생성되었습니다. (ID: {self.id})")

    def __del__(self):
        print(f"🗑️ {self.name} 주소록 인스턴스가 삭제되었습니다. (현재 카운트: {Address.auto_increment})")

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        print("name의 getter 호출됨!")
        return self.__name

    @name.setter
    def name(self, name):
        print("name의 setter 호출됨!")
        self.__name = name

    @property
    def phone(self):
        print("phone의 getter 호출됨!")
        return self.__phone

    @phone.setter
    def phone(self, phone):
        print("phone의 setter 호출됨!")
        self.__phone = phone

    # + 연산자 오버로딩
    def __add__(self, other):
        return self.name + other.name
    
    # 인스턴스를 호출했을 때 리턴되는 문자열 관련 메서드
    def __str__(self):
        return str(self.__id)

# --- 테스트 코드 ---
address1 = Address("홍길동", "010-1234-5678")
address2 = Address("전우치", "010-8765-4321")
# __add__(self,other)를 Overloading 하지 않으면 에러
result = address1 + address2
print(result)  # 홍길동전우치

print(address1)