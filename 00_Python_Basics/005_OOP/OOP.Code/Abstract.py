import abc

# 추상 클래스 - 인스턴스를 생성할 수 없습니다.
class Super(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def method(self):
        pass

# 추상 클래스를 상속받으면 하위 클래스에서는 추상 메서드를 반드시 구현해야 합니다.
class Sub(Super):
    def method(self):
        print("추상 메서드 구현")

sub = Sub()
sub.method()

