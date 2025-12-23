# 🛠️ Python: 클래스 고급 기능 및 데이터 보호

## 1. 클래스 레벨 메서드 (Static & Class Method)

인스턴스를 생성하지 않고 클래스 이름으로 직접 호출하는 메서드들입니다.

| **구분** | **Static Method** | **Class Method** |
| --- | --- | --- |
| **데코레이터** | `@staticmethod` | `@classmethod` |
| **첫 번째 매개변수** | 없음 (self 사용 불가) | **cls** (클래스 자신) |
| **특징** | 일반 함수와 비슷하나 클래스 내부에 위치함 | 상속 시 호출한 클래스를 인지함 |
| **주요 용도** | 클래스 변수의 초기화 및 유틸리티 | 클래스 속성 제어, **팩토리 메서드** |

---

## 2. 속성 동적 생성과 `__slots__`

파이썬은 실행 중(Runtime)에 인스턴스 속성을 자유롭게 추가할 수 있는 유연한 언어입니다.

### ⚠️ 동적 생성의 위험성

- **일관성 결여**: 클래스 설계 시 의도하지 않은 속성이 마구잡이로 생길 수 있음.
- **메모리 낭비**: 내부적으로 `__dict__`를 통해 속성을 관리하므로 메모리 사용량이 많음.

> 💡 CS 인사이트
> 
> 
> 이는 **NoSQL(Schema-less)**과 **RDBMS(Schema-fixed)**의 차이와 유사합니다.
> 
> - **유연함 vs 엄격한 구조**의 트레이드오프를 이해하는 것이 중요합니다.

### 🔒 `__slots__`를 통한 제한

클래스에 `__slots__`를 정의하면 리스트에 명시된 속성 이외에는 생성할 수 없도록 강제하며, 메모리 효율을 극대화합니다.

```python
class Address:
    # 지정된 속성 이외의 동적 생성 차단
    __slots__ = ['id', 'name', 'phone']

    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
```

---

## 3. 접근 지정자 (Access Modifier)

데이터에 대한 직접 접근을 제한하여 **캡슐화(Encapsulation)**를 실현합니다.

- **Public (기본값)**: 어디서든 접근 가능.
- **Private (`__`)**: 속성 이름 앞에 언더바 두 개를 붙여 외부 직접 접근을 차단.

### 📑 실무 권장 사항 (Getter / Setter)

속성을 직접 변경하기보다 검증 로직이 포함된 접근자 메서드를 사용하는 것을 권장합니다.

```python
class Address:
    __slots__ = ["__id", "__name", "__phone"] # Private 변수들만 허용

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def set_name(self, name):
        # 검증 로직 추가 가능
        self.__name = name

    def get_name(self):
        return self.__name

# [테스트 코드]
address = Address("홍길동", "010-1234-5678")

# address.__name = "adam"  # ❌ Error 발생 (직접 접근 불가)
address.set_name("adam")   # ✅ 메서드를 통한 안전한 변경
print(address.get_name())`
```

---

## 4. Property (프로퍼티)

### 1️⃣ Property란?

속성에 접근할 때 메서드를 거치도록 만드는 기법입니다. **사용자 입장에서는 변수처럼 보이지만, 내부적으로는 함수가 실행**됩니다.

- **Getter**: 값을 읽어올 때 실행.
- **Setter**: 값을 대입할 때 실행 (유효성 검사 수행).

### 2️⃣ 생성 방법 비교

### 방법 A: `property()` 함수 사용 (수동 연결)

```python
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        print(f"이름을 {value}로 변경합니다.")
        self._name = value

    # 변수명 = property(fget, fset)
    name = property(fget=get_name, fset=set_name)
```

### 방법 B: 데코레이터(`@`) 사용 (권장 방식)

```python
class Person:
    def __init__(self, name):
        self._name = name  # 실제 데이터 저장 변수

    @property # Getter
    def name(self):
        return self._name

    @name.setter # Setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("이름은 문자열이어야 합니다.")
        print(f"이름을 {value}로 변경합니다.")
        self._name = value
```

---

## 💡 핵심 요약

- **왜 쓰나요?** : `p.name = "값"`처럼 직관적인 코드를 유지하면서도, 내부적으로는 **값 검증(Validation)**이나 로그 출력을 수행하기 위해서입니다.
- **주의사항** : 실제 값을 담는 변수는 `self._name`처럼 프로퍼티 이름과 다르게 설정해야 합니다. (이름이 같으면 무한 루프/Recursion Error 발생!)

---

## ➕5. 연산자 오버로딩

### 1️⃣ 핵심 개념 비교

객체지향 프로그래밍(OOP)에서 가장 혼동하기 쉬운 두 개념을 정리합니다.

| **구분** | **Overriding (재정의)** | **Overloading (과적/다중정의)** |
| --- | --- | --- |
| **정의** | 상위 클래스의 메서드를 하위 클래스에서 **다시 정의**함 | 동일 클래스 내에서 **매개변수/자료형**을 다르게 구성함 |
| **목적** | 상속받은 기능의 **확장 및 변경** (매우 중요!) | 동일 이름의 메서드에 **다양한 연산 기능** 부여 |
| **파이썬 특징** | `super()` 등을 활용해 부모 기능을 가져옴 | 파이썬은 **매직 메서드(Magic Method)**를 통해 구현 |

### 2️⃣ 연산자 오버로딩 상세

- **정의**: 인스턴스끼리 연산(`+`,  등)을 할 수 있도록 기존 연산자의 기능을 클래스에 맞춰 변경하는 것.
- **작동 원리**: 특정 이름의 **매직 메서드**를 정의하면 파이썬 인터프리터가 이를 인식합니다.
    - 이미 정의된 기능이 있다면 **변경(Override)**되고, 없다면 새로운 기능이 **추가**됩니다.

### 📑 주요 매직 메서드

- `__add__(self, other)`: `+` 연산 시 호출
- `__str__(self)`: `print()`나 `str()` 호출 시 인스턴스를 문자열로 리턴

```python
class Address:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # [Overloading] + 연산자 정의
    def __add__(self, other):
        return f"{self.name} & {other.name}의 연락처가 병합되었습니다."

address1 = Address("홍길동", "010-1234-5678")
address2 = Address("전우치", "010-8765-4321")

# __add__를 정의하지 않으면 에러 발생
result = address1 + address2 
print(result) # 출력: 홍길동 & 전우치의 연락처가 병합되었습니다.
```

---

## 👆7. 싱글톤 패턴 (Singleton Pattern)

### 1️⃣ 정의 및 목적

- **정의**: 클래스의 인스턴스를 **단 1개만** 생성하도록 제한하는 디자인 패턴입니다.
- **목적**: 프로그램 전체에서 특정 자원(DB 연결, 설정 파일 등)에 접근하는 객체를 하나로 강제하여 **일관성**을 유지하고 **메모리**를 절약합니다.

### 2️⃣ 객체 비교의 이해 (`is` vs `==`)

싱글톤을 이해하기 위해선 객체의 주소값을 비교하는 `is` 연산자의 동작을 알아야 합니다.

```python
address1 = Address("홍길동", "010-1234-5678")
address2 = Address("홍길동", "010-1234-5678")

print(address1 is address2) # False
# 이유: 내부 데이터(값)는 같지만, 생성된 인스턴스의 ID(메모리 주소)가 다르기 때문
```

### 3️⃣ 싱글톤 구현 (Pythonic Way)

`__new__` 메서드를 오버라이딩하여 인스턴스 생성을 직접 제어합니다.

```python
class Singleton:
    __instance = None # 인스턴스를 저장할 클래스 변수

    def __new__(cls, *args, **kwargs):
        # 인스턴스가 없을 때만 딱 한 번 생성
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

# 싱글톤 상속 활용
class Sub(Singleton):
    a = 10

sub1 = Sub()
sub2 = Sub()

print(sub1 is sub2) # True (완전히 동일한 인스턴스임을 증명)`
```

---

> 💡 CS 인사이트
> 
> 
> 파이썬에서 *args와 **kwargs를 __new__에 쓰는 이유는, 싱글톤을 상속받는 하위 클래스들이 어떠한 매개변수를 가져오더라도 에러 없이 부모의 생성 로직을 통과시키기 위함입니다. 일종의 **"범용적인 통로"**를 만들어 두는 것이죠!
> 

---

## 🧑‍🍼8. Inheritance (상속)

### 📝 개요

상위 클래스의 모든 속성과 메서드를 하위 클래스가 물려받는 것입니다.

- **Super (Base) 클래스:** 기능을 물려주는 상위 클래스
- **Sub (Derived) 클래스:** 기능을 물려받는 하위 클래스
- **단일 상속:** 하나의 클래스로부터 상속
- **다중 상속:** 여러 개의 클래스로부터 상속

### 🎯 상속의 목적

1. **코드 중복 제거:** 여러 클래스에서 공통으로 사용하는 코드를 상위 클래스에 한 번만 정의
2. **기능 확장:** 기존 클래스의 기능을 유지하면서 새로운 기능을 추가하거나 수정

---

## 🛠 상속 형식 및 기초

### 1. 상속 문법

```python
class 클래스이름(상위클래스이름1, 상위클래스이름2...):
    # 클래스 내용`
```

### 2. 상속 전 vs 후 비교

| **구분** | **상속 전** | **상속 후** |
| --- | --- | --- |
| **특징** | 각 클래스가 독립적임 | `Sub`가 `Super`를 포함함 |
| **결과** | `Sub`에서 `Super` 메서드 호출 시 에러 | `Sub`에서 `Super` 메서드 자유롭게 사용 |

**[코드 예시: 상속 후]**

```python
class Super:
    def greeting(self):
        print("상위 클래스의 메서드")

class Sub(Super): # 상속 선언
    def insa(self):
        print("하위 클래스의 메서드")

sub = Sub()
sub.greeting()  # 상위 클래스 메서드 호출 가능
sub.insa()      # 하위 클래스 메서드 호출
```

---

## 🏗 생성자 (`__init__`)와 상속

하위 클래스에서 상위 클래스의 속성을 사용하려면 메모리에 상위 클래스의 인스턴스가 먼저 생성되어야 합니다.

### 1. 묵시적 호출

하위 클래스에 `__init__`이 정의되어 있지 않다면, 파이썬이 자동으로 상위 클래스의 `__init__`을 호출합니다.

### 2. 명시적 호출 (`super()`)

상위 클래스의 `__init__`에 **매개변수**가 필요한 경우, 하위 클래스에서 반드시 `super().__init__(매개변수)`를 통해 명시적으로 호출해야 합니다.

```python
class Super:
    def __init__(self, name):
        self.name = name
        print("Super의 init")

class Sub(Super):
    def __init__(self):
        # 상위 클래스의 생성자에 필요한 인자를 전달하며 명시적 호출
        super().__init__("홍길동") 
        print("Sub의 init")

    def insa(self):
        print(f"{self.name}님, 안녕하세요.")

sub = Sub()
sub.insa()
```

---

## 🔄 Method Overriding (메서드 재정의)

상위 클래스에 정의된 메서드를 하위 클래스에서 **자신의 용도에 맞게 다시 정의**하는 것입니다.

### 💡 핵심 개념: 계란 모델

> 🥚 계란 노른자(상위 클래스) 를 계란 흰자(자식 클래스) 가 감싸고 있는 형태라고 생각하세요.
> 
> 
> 기능을 확장할 때 노른자의 기능을 먼저 쓰고 흰자의 기능을 덧붙이는 방식입니다.
> 
- **실행 순서:**
    1. **생성 시:** 상위 클래스 생성자 → 하위 클래스 생성자
    2. **소멸 시:** 하위 클래스 소멸자 → 상위 클래스 소멸자

### 💻 오버라이딩 예시

```python
class Super:
    def greeting(self):
        print("상위 클래스의 메서드")

class Sub(Super):
    def greeting(self):
        super().greeting() # 상위 클래스의 기존 기능을 먼저 수행
        print("하위 클래스에서 추가된 기능") # 기능 확장

sub = Sub()
sub.greeting()
# 출력:
# 상위 클래스의 메서드
# 하위 클래스에서 추가된 기능
```

---

## 👨‍👨‍👦 9. 다중 상속 & 추상화 (Abstract)

## 1. 다중 상속 (Multiple Inheritance)

### 📌 개요

- **정의:** 하위 클래스가 두 개 이상의 상위 클래스로부터 속성과 기능을 물려받는 것.
- **비유:** **스마트폰** (디지털 카메라 + MP3 플레이어 + 전화기 등 여러 기능의 결합)

### ⚠️ 특징 및 주의사항

- **확장성:** 여러 클래스의 기능을 모을 수 있어 확장이 매우 빠름.
- **유지보수의 어려움:** 상위 클래스 중 하나만 수정되어도 하위 클래스에 예기치 못한 영향을 미침 (스마트폰의 수명이 상대적으로 짧은 이유와 유사).
- **중복 문제:** 상위 클래스들에 동일한 이름의 메서드가 있을 경우, 어떤 것을 가져올지 결정하는 순서가 복잡해짐. → **권장되지 않는 패턴**

---

### 💻 다중 상속 구현

```python
# 다중 상속 형식
class 상위클래스1:
    def method1(self):
        print("Super1의 Method")

class 상위클래스2:
    def method2(self):
        print("Super2의 Method")

# 여러 클래스를 나열하여 상속
class Sub(상위클래스1, 상위클래스2):
    pass

sub = Sub()
sub.method1()
sub.method2()
```

---

### 🔍 MRO (Method Resolution Order)

다중 상속 시 동일한 메서드가 존재할 때 호출되는 순서를 결정하는 알고리즘입니다.

> 💡 mro() 확인하기
> 
> 
> 클래스이름.mro()를 호출하여 탐색 순서를 리스트 형태로 확인할 수 있습니다.
> 

```python
class Super:
    def method(self):
        print("Super1의 Method")

class Super2:
    def method(self):
        print("Super2의 Method")

class Sub(Super, Super2): # 나열된 순서가 우선순위가 됨
    pass

sub = Sub()
sub.method()  # Super(첫 번째 상속 클래스)의 method가 호출됨
print(Sub.mro()) # [<class 'Sub'>, <class 'Super'>, <class 'Super2'>, <class 'object'>]
```

---

## 2. 추상 (Abstract) : Template Programming

### 📋 개념 이해

- **Template (원형/모양):** 무엇을 만들지 정의하는 설계도.
- **Implementation (구현/내용):** 실제 세부 동작을 코드로 작성하는 것.
- **비유:** * **메뉴판(추상)**과 **음식(구현)**
    - C언어의 **헤더파일(.h)**과 **소스파일(.c)**

### 🛠 추상 클래스와 인터페이스

| **구분** | **특징** |
| --- | --- |
| **인터페이스(Interface)** | 오직 Template(원형)만 가질 때 (파이썬에서는 프로토콜이라고도 함) |
| **추상 클래스** | Template과 실제 구현 내용을 함께 가질 수 있음 |

---

### ⚖️ 추상 메서드와 추상 클래스

1. **추상 메서드:** 내용이 없는 메서드로, 하위 클래스에서 **반드시 구현(Overriding)** 해야 함.
2. **추상 클래스:** 인스턴스를 직접 만들 수 없는 클래스. 반드시 1개 이상의 추상 메서드를 포함해야 함.

---

### ⚙️ 파이썬에서 구현하는 방법

파이썬은 `abc` (Abstract Base Class) 모듈을 사용합니다.

1. `import abc`
2. 클래스 선언 시 `(metaclass = abc.ABCMeta)` 추가
3. 추상 메서드 위에 `@abc.abstractmethod` 데코레이터 추가

```python
import abc

# 1. 추상 클래스 선언 (설계도)
class Login(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def login(self, id, pw):
        pass # 내용은 작성하지 않음

# 2. 실제 구현 클래스
class LoginImp1(Login):
    def login(self, id, pw):
        # 자식 클래스에서 반드시 구체적인 내용을 작성해야 함
        print(f"{id} 계정으로 로그인을 수행합니다.")

# test = Login() # 에러: 추상 클래스는 직접 인스턴스 생성 불가
user = LoginImp1()
user.login("seongyun", "1234")
```

---

### 🚀 마이크로 서비스 (Microservice)

- **구조:** 하나의 요청 → 하나의 메서드 → 하나의 클래스
- **장점:** 기능이 쪼개져 있어 재사용성이 매우 높음.
- **추상화의 역할:** 시스템을 서비스 단위로 쪼개기 전, 전체적인 구조(Template)를 잡는 데 핵심적인 역할을 함.

---

## 🎭 10. 다형성 (Polymorphism)

### 1. 추상화 전: 개발자와 유저의 관점 차이

동일한 기능(공격)임에도 불구하고 개발자마다 메서드 이름을 다르게 정의하면, 이를 사용하는 유저(호출자)는 각 클래스의 메서드 이름을 모두 외워야 하는 불편함이 발생합니다.

**💻 코드 예시**

```python
# 개발자의 관점 (구현)
class Terran:
    def attack(self):
        print("테란의 공격")

class Zerg:
    def attack(self):
        print("저그의 공격")

class Protoss:
    def offense(self): # 동일한 기능이지만 이름이 다름 (공격)
        print("프로토스의 공격")

# 유저의 관점 (실행)
star = Terran()
star.attack()

star = Zerg()
star.attack()

star = Protoss()
star.offense() # 유저는 Protoss만 'offense'임을 따로 기억해야 함 (불편)
```

---

### 2. 추상화 후: 강제성을 통한 인터페이스 통일

`abc` 모듈을 사용하여 상위 클래스에서 메서드 이름을 **강제**하면, 모든 하위 클래스가 동일한 이름의 메서드를 가지게 되어 유저가 사용하기 훨씬 편리해집니다.

**💻 코드 예시**

```python
import abc

# 상위 클래스 (Template): 모든 종족은 'attack'이라는 이름을 써야 한다고 규정
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
    # 만약 추상 메서드인 attack을 구현하지 않고 offense를 쓰면 에러 발생!
    def attack(self): 
        print("프로토스의 공격")

# 유저의 관점 (실행) - 이제 모든 종족을 'attack()'으로 제어 가능
units = [Terran(), Zerg(), Protoss()]

for unit in units:
    unit.attack() # 어떤 종족인지 몰라도 attack()만 부르면 됨 (다형성)
```

---

### 💡 핵심 요약

- **문제점:** 기능은 같은데 이름이 다르면(attack vs offense) 코드의 재사용성과 일관성이 떨어짐.
- **해결책:** **추상 클래스(ABC)**를 통해 하위 클래스들이 동일한 메서드 이름을 구현하도록 강제함.
- **결과:** 유저는 내부 구현을 몰라도 **하나의 인터페이스(attack)**만 알면 모든 객체를 다룰 수 있음 (**다형성 완성**).

---