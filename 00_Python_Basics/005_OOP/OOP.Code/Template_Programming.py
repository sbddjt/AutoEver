import abc

# 실제 구현할 기능의 원형만 선언
class Login(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def login(self, id, pw):
        pass

# 실제 내용을 구현
class LoginImp1(Login):
    def login(self, id, pw):
        print("id와 pw를 가지고 로그인을 수행합니다.")
    

user = LoginImp1()
user.login("adam", "1234")