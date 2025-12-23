import abc

class Star(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def attack(self):
        pass

class Terran(Star):
    def attack(self):
        print("테란의 공격")

class Zerg(Star):
    def attack(self):
        print("저그의 공격")

class Protoss(Star):
    def attack(self):
        print("프로토스의 공격")


star = Terran()
star.attack()
star = Zerg()
star.attack()
star = Protoss()
star.attack() # 에러 attack() 안 씀
