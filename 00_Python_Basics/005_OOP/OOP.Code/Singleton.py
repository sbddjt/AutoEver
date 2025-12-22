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

# 싱글톤 클래스를 만들기 위한 상위 클래스
class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance
    

# 싱글톤 클래스를 상속받으면 이 클래스는 싱글톤 디자인 패턴을 적용한 클래스가 됩니다.
class Sub(Singleton):
    a = 10

sub1 = Sub()
sub2 = Sub()
print(sub1 is sub2)