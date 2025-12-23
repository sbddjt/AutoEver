class Address:
    auto_increment = 1

    # 속성을 제한하는 속성
    __slots__ = ['id', 'name', 'phone']

    def __init__(self, name, phone="전화번호없음"):
        self.id = Address.auto_increment
        self.name = name
        self.phone = phone
        Address.auto_increment += 1
        print(f"✨ {self.name} 주소록 인스턴스가 생성되었습니다. (ID: {self.id})")

    def __del__(self):
        Address.auto_increment -= 1
        print(f"🗑️ {self.name} 주소록 인스턴스가 삭제되었습니다. (현재 카운트: {Address.auto_increment})")

    # 접근자 메서드 (Getter)
    def get_id(self): return self.id
    def get_name(self): return self.name
    def get_phone(self): return self.phone

# --- 테스트 코드 ---

address = Address(name="홍길동", phone="010-1234-5678")
address.hometown = "서울"  # __slots__로 인해 새로운 속성 추가 불가

