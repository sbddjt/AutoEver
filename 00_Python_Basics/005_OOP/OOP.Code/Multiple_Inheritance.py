class Super:
    def method(self):
        print("Super1의 Method")

class Super2:
    def method(self):
        print("Super2의 Method")

class Sub(Super, Super2):
    pass

sub = Sub()
sub.method()  # Super 클래스의 method가 호출됩니다.
print(Sub.mro())

