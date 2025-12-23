class Address:
    auto_increment = 1

    # Static Method: 클래스나 인스턴스 정보가 필요 없을 때 사용
    @staticmethod
    def method1(initValue):
        print(f"--- Static Method: 초기값을 {initValue}로 강제 설정합니다. ---")
        Address.auto_increment = initValue

    # Class Method: 클래스 자체(cls)에 접근할 때 사용 (추천 방식)
    @classmethod
    def method2(cls, initValue):
        print(f"--- Class Method: {cls.__name__} 클래스의 변수를 {initValue}로 초기화합니다. ---")
        cls.auto_increment = initValue

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