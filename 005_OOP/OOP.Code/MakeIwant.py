class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100 # 기본 체력

    # 데이터 내보내기 (Getter)
    def get_hp(self):
        return self.hp

    # 데이터 수정하기 (Setter)
    def set_hp(self, amount):
        self.hp = amount
        if self.hp <= 0:
            print(f"💀 {self.name}님이 쓰러졌습니다!")
        else:
            print(f"❤️ {self.name}의 현재 체력: {self.hp}")

# 인스턴스 생성 및 활용
p1 = Player("전사")

# Getter로 체력 확인
current_hp = p1.get_hp()
print(f"{p1.name}의 시작 체력: {current_hp}")

# Setter로 체력 수정 (데미지 입음)
p1.set_hp(70)  # 30 데미지 입음
p1.set_hp(30)  # 40 데미지 입음
p1.set_hp(0)   # 30 데미지 입음, 쓰러짐

    
    

