class Address:
    auto_increment = 1

    __slots__ = ['__id', '__name', '__phone']

    def __init__(self, name, phone="전화번호없음"):
        self.__id = Address.auto_increment
        self.__name = name
        self.__phone = phone
        Address.auto_increment += 1
        print(f"✨ {self.__name} 주소록 인스턴스가 생성되었습니다. (ID: {self.__id})")

    def __del__(self):
        Address.auto_increment -= 1
        print(f"🗑️ {self.__name} 주소록 인스턴스가 삭제되었습니다. (현재 카운트: {Address.auto_increment})")
    
    # 접근자 메서드 (Getter)
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_phone(self): return self.__phone

    # 지정자 메서드 (Setter)
    def set_name(self, name): self.__name = name
    def set_phone(self, phone): self.__phone = phone

# --- 테스트 코드 ---
address = Address("홍길동","010-1234-5678")

#인스턴스를 통해서 속성을 직접 접근 : __를 붙이면 private이 되서 인스턴스가 접근 불가능해서 에러
address.__name = "adam"


