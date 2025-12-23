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
        Address.auto_increment -= 1
        # 안전한 참조를 위해 직접 접근
        name = getattr(self, '_Address__name', '알 수 없음')
        print(f"🗑️ {name} 주소록 인스턴스가 삭제되었습니다. (현재 카운트: {Address.auto_increment})")

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print("name의 setter 호출됨!")
        # self.__name(기존값)이 아닌 인자로 들어온 name(새값)의 길이를 체크해야 함
        if len(name) >= 3:
            print("이름이 너무 깁니다.")
            if not hasattr(self, '_Address__name'):
                self.__name = "무명"
            return
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

# --- 테스트 코드 ---
# "홍길동"은 3글자이므로 setter 조건에 의해 "무명"으로 생성됨
address = Address("홍길동", "010-1234-5678")

# "adam"은 4글자이므로 수정되지 않음
address.name = "adam" 
print(f"현재 이름: {address.name}")