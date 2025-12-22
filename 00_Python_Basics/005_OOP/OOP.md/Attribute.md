## Getter와 Setter (접근자 메서드)

객체 지향에서는 속성에 직접 접근(`obj.num = 10`)하는 것보다 메서드를 거치는 것을 권장합니다. (정보 은닉 및 데이터 무결성 유지)

### 🔍 Getter (획득자)

- **역할**: 속성값을 읽어올 때 사용.
- **규칙**:
    - 이름: `get_속성명` (Python 관례: 소문자와 언더바 사용).
    - 매개변수: 없음.
    - 내용: 속성값을 `return` 함.
    - **특이사항**: bool 타입은 `is_속성명`, 컨테이너 타입은 인덱스를 받아 해당 데이터를 리턴하기도 함.

### 🖋️ Setter (설정자)

- **역할**: 속성값을 수정할 때 사용.
- **규칙**:
    - 이름: `set_속성명`.
    - 매개변수: 수정할 데이터.
    - 내용: 매개변수로 내부 속성값을 수정함.

---

## 💻 코드 실습 및 ID 분석

이 코드는 클래스 변수가 인스턴스 변수로 어떻게 분리되는지 `id()`를 통해 증명합니다.

```python
# 클래스
class Address:
    # 클래스가 소유하는 변수
    num = 0

# Address 클래스의 인스턴스 생성
address = Address()
print(Address.num)
print(address.num)
print("------------")
# 클래스를 이용해서 수정
Address.num = 10
print(Address.num)
print(address.num)
print(id(Address.num))
print(id(address.num))
print("------------")
# 인스턴스를 이용해서 수정: 인스턴스 안에 별도로 생성하고 클래스의 속성은 변경하지 않음
address.num = 20
print(Address.num)
print(address.num)
print(id(Address.num))
print(id(address.num))
print("------------")
```

![image.png](attachment:4aedca7a-ccf5-4935-af3a-7bc94c4571fa:image.png)

---

## 4. 인스턴스가 소유하는 속성

- **정의**: 메서드 안에서 `self.속성이름`을 사용하여 선언되는 속성.
- **특징**:
    - 클래스 전체가 아닌 해당 인스턴스 전용 저장소(Heap)에 생성됩니다.
    - 메서드가 **처음 호출될 때** 메모리에 생성됩니다.