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

# 1. 초기 생성 (ID: 1)
address = Address(name="홍길동", phone="010-1234-5678")
print(f"홍길동 ID: {address.get_id()}")

# 2. 소멸 유도 (카운트 2 -> 1로 감소)
address = None 

# 3. 클래스 메서드를 이용한 번호표 강제 재설정
Address.method2(100) # auto_increment를 100으로 변경

# 4. 새로운 인스턴스 생성 (ID: 100)
address2 = Address(name="김철수", phone="010-9876-5432")
print(f"김철수 ID: {address2.get_id()}")

address3 = Address(name="이영희")
print(f"이영희 ID: {address3.get_id()}")