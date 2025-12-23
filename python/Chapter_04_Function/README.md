# 📦Function (함수) - 구조적 설계와 모듈화

## 1. 정의

- **개념**: 한 번에 실행되어야 하는 문장들을 하나의 이름으로 묶어서 독립적으로 실행할 수 있도록 하는 것
- **참조 vs 호출**:
    - **함수의 이름만 호출**: 함수의 **참조**(메모리 주소)가 됨
    - **함수이름()**: 함수의 **호출**(실행)을 의미

### 💡 함수 사용의 장점

- **유지보수 편리**: 함수 이름과 매개변수를 대입해 호출하면 내부 코드가 실행되므로, 동일 코드를 여러 번 사용하는 경우 코드 중복을 제거할 수 있음 (DRY 원칙)

---

## 2.  메모리 구조와 Stack

함수를 호출하면 메모리상에 **Stack** 자료구조가 생성됩니다.

- **스택 오버플로우(Stack Overflow) 방지**:
    - `main()` 함수 하나에 모든 코드를 넣으면 메모리 한계를 초과할 수 있음
    - 함수를 적절히 분리하여 호출하고 종료(메모리 해제)함으로써 스택 공간을 효율적으로 사용해야 함
- **할당 단위**: 보통 Stack은 **1MB 단위**로 할당됨. 따라서 `main()`에 너무 많은 데이터를 한꺼번에 처리하도록 설계하면 안 됨

---

## 3. 함수의 종류

1. **Built-In Function (내장 함수)**:
    - 파이썬 언어 자체에서 기본적으로 제공하는 함수 (Maker Function)
    - (`dir(__builtins__)`로 확인 가능)
        
        ![image.png](attachment:3a7c621e-1e65-4e18-90dc-892265915bc8:image.png)
        
2. **User-Defined Function (사용자 정의 함수)**: 개발자가 필요에 의해 직접 만든 함수

---

## 4.  파이썬 함수는 일급 객체 (First-class Object)

파이썬에서 함수는 단순한 실행 단위가 아니라 **하나의 데이터(자료형)**로 취급됩니다.

### 📌 주요 특징

1. **변수에 대입 가능**: 함수를 변수에 할당하여 다른 이름으로 호출할 수 있음
2. **매개변수로 사용 가능**: 다른 함수의 인자로 함수를 전달할 수 있음 (고차 함수)
3. **결과로 리턴 가능**: 함수의 결과값으로 또 다른 함수를 반환할 수 있음
4. **Runtime 생성 가능**: 컴파일 타임이 아닌 프로그램 실행 중에 함수를 생성하고 정의할 수 있음

---

## 5. [비교] C언어 vs 파이썬 (정적 vs 동적)

### ⚙️ C언어 (Compile Time 중심)

- **정적 준비**: 서버 프로그래밍처럼 미리 모든 자원을 준비해야 하는 경우에 유리함
- **작성 방식**: C

```python
int a = 1;
int b = 2; // 미리 공간을 확보
a = 2;     // 나중에 변경
```

- **주의**: 선언과 할당의 순서가 중요하며, 실행 중에 구조를 바꾸기 어려움

### 🐍 파이썬 (Runtime 중심)

- **동적 프로그래밍**: 클라이언트 프로그래밍이나 빠른 실행이 필요한 환경에서 유리함
- **특징**: 실행 중에 함수를 만들거나 변수의 타입을 바꾸는 등 유연한 처리가 가능함

---

## 6. 함수 정의 및 리턴 (Return)

### 🔹 기본 형식 및 Type Hinting

최근에는 가독성을 위해 **리턴 타입**과 **인수 타입**을 명시하는 것을 권장합니다.

```python
def interAddWithInteger(first: int, second: int) -> int:
    """정수 2개를 더해서 리턴하는 함수"""
    result = first + second
    return result

# 호출
k = interAddWithInteger(20, 30)
```

### 🔹 리턴의 특징

- **모든 함수는 리턴값을 가짐:** 명시적 `return`이 없으면 `None`을 반환.
- **실행 중단:** `return`을 만나는 즉시 함수 종료 (**Dead Code** 주의).
- **여러 데이터 리턴:** `,`(쉼표)로 구분하여 리턴하면 실제로는 하나의 **튜플(Tuple)**로 묶여 반환됨.

---

## 7. argument(인수, 인자)

- **정의**: parameter라고 하기도 하며, 함수를 호출할 때 넘겨주는 데이터입니다.
- **역할**: 함수 내부에서 이 데이터를 가지고 처리를 수행한 후 결과를 돌려주거나 데이터에 변형을 가하게 됩니다.
- **작성 관례 (Type Hinting)**:
    - 예전에는 인수의 이름만 작성했습니다.
    - 최근에는 **`이름: 자료형`*의 형태로 명시적으로 자료형을 기재하는 것을 권장합니다.

```python
def tupleReturn(first : int, second : int) -> tuple: # 반환되는 자료형을 되도록 쓰자
    result1 = first + second
    result2 = first - second
    return (result1, result2)

print(tupleReturn(100, 200))
```

- **필수성**: 인수에 아무런 기호(기본값 등)가 없다면 인수는 함수를 호출할 때 반드시 데이터를 대입해야 합니다.

### 1) 데이터 전달 방식

매개변수에 전달되는 데이터의 종류에 따라 처리 방식이 달라집니다.

- **스칼라 데이터 (Scalar)**:
    - **방식**: 값을 **복사**해서 넘겨줍니다.
    - **특징**: 함수 내부에서 값을 변경해도 원본 데이터에는 영향을 주지 않는 'Call by Value'의 성격을 가집니다.

```python
# 스칼라 데이터를 넘겨주면 데이터를 복사해서 넘겨줍니다.
# 함수 내부에서 데이터를 변경해도 원본에는 영향이 없습니다.
def callByValue(a : int) -> None:
    print("a: ", a)
    a = a + 1
    print("a: ", a)

x = 10
callByValue(x)
print("x: ", x)
```

![image.png](attachment:5ce69c7f-f2f1-4c05-94f1-51e78f065b8f:image.png)

- **벡터 데이터 (Vector/Container)**:
    - **방식**: **참조(Reference)를 복사**해서 넘겨줍니다.
    - **특징**: 리스트나 딕셔너리 같은 컨테이너는 주소값을 공유하므로, 함수 내부에서 원본 데이터에 직접 접근이 가능합니다.

```python
# 벡터 데이터를 넘겨주면 데이터의 참조를 넘겨줍니다.
# 함수 내부에서 데이터의 참조를 받아서 세부 데이터를 수정하면 원본도 같이 수정됩니다.
def callByReference(li : list) -> None:
    print("li: ", li)
    li[0] = li[0] + 1
    print("li: ", li)

l = [10, 20]
callByReference(l)
print("l: ", l)
```

![image.png](attachment:06640ba7-8433-46f5-b686-2a4f32df8b6b:image.png)

### **2) Keyword Arguments (이름을 이용한 매개변수 전달)**

- **이름 기반 데이터 전달**: 함수를 호출할 때 매개변수의 이름과 함께 데이터를 넘기는 것이 가능합니다.
- **순서 변경 가능**: 이렇게 이름을 사용하면 인자의 순서를 변경해서 대입하는 것도 가능합니다.

**📝 실습 코드 예시**

```python
def sub(first : int, second : int) -> int:
    result = first - second
    return result

# 1. 위치 기반 호출 (Positional Arguments)
print(sub(100, 200))
# 2. 이름을 사용해서 매개변수를 설정 (Keyword Arguments)
print(sub(first = 100, second = 200))
# 3. 이름을 사용하면 순서를 변경해도 무관함
print(sub(second = 200, first = 100))
```

---

### **3) Default Parameter Value (매개변수 기본값 설정)**

**개요**: 파이썬에서는 매개변수를 만들 때 기본 값을 설정하는 것이 가능합니다.

```python
def 함수이름 (이름 : 자료형 = 기본값...) -> 리턴 타입:
    # 문장 나열
```

- **동작 방식**: 기본값이 있는 매개변수는 호출할 때 생략 가능한데, 생략하면 설정된 **기본값**으로 작업을 수행합니다.
- **작성 규칙**: 한 번 기본값이 설정되면 **그 이후의 매개변수는 전부 기본값을 설정**해야 합니다.
    
    > (예: 중간에 있는 매개변수만 기본값을 주고 그 뒤를 비워둘 수 없습니다.)
    > 

**📝 실습 코드 예시**

```python
def sub(first : int, second : int = 0) -> int:
    result = first - second
    return result

print(sub(first = 100, second = 200))
print(sub(first = 100))
```

---

## 8. 순수 함수, 비순수 함수

### 🟢 순수 함수 (Pure Function)

- **정의**: 입력하는 데이터가 같으면 항상 동일한 결과를 리턴하는 함수입니다.
- **특징**:
    - 입력하는 데이터를 수정하지 않는 함수입니다.
    - 함수의 실행이 외부 상태에 영향을 끼치지 않는 함수입니다.
    - side effect(부작용)가 없어야 하고 입력 값이 같으면 언제나 동일한 출력 값을 반환합니다.

### 🔴 비순수 함수 (Impure Function)

- **정의**: 함수의 실행이 외부 상태에 영향을 끼치는 함수입니다.
- **특징**:
    - **modifier function** 이라고도 합니다.
    - 함수 내부에서 외부 변수를 수정하거나, 입출력(I/O) 작업을 수행하여 실행할 때마다 결과가 달라질 수 있습니다.

---

## 9. 매개변수 언패킹 (Parameter Unpacking)

파이썬은 함수 호출 시 컨테이너에 담긴 데이터를 개별 매개변수로 풀어서 전달하는 **언패킹 기능**을 제공합니다.

1. **시퀀스 언패킹 (*)**
- **대상**: `list`, `tuple`, `set` 등의 데이터를 대입할 때 사용합니다.
- **동작**: 컨테이너 앞에 ***을 붙여서 대입하면 자동으로 압축이 해제되어, 컨테이너 내부의 데이터가 순서대로 매개변수에 대입됩니다.

1. **딕셔너리 언패킹 (**)**
- **대상**: `dict` 데이터를 대입할 때 사용합니다.
- **동작**:
    - 단순히 대입하면 **Key**만 대입됩니다.
    - *`*`*을 이용해서 대입하면, **매개변수 이름과 대응되는 Key 이름**을 찾아 데이터를 자동으로 매칭하여 대입합니다.

```python
def sub(first : int, second : int) -> int:
    result = first - second
    return result

print(sub(first = 100, second = 70))
# container를 *과 함께 대입하면 분할해서 대입이 됩니다.
print(sub(*[100,70]))
# dict를 대입할 때 **을 붙여서 대입하면 key와 일치하는 매개변수에 데이터가 대입됩니다.
print(sub(**{"first" : 100, "second" : 70}))
```

## 10. 가변 매개변수

- 매개변수의 개수에 상관없이 대입받도록 하는 문법
- *을 이용해서 정의하면 매개변수를 tuple 만들어서 사용하고 **을 이용해서 정의하면 dict가 만들어집니다.

```python
def tot(*arg):
    result = 0
    for x in arg:
        result = result + x
    return result

print(tot(10, 20))
print(tot(10, 20, 30))
print(tot(10, 20, 30, 40))
```

![image.png](attachment:ade1e2fa-8b69-4898-bb25-f709d3995160:image.png)

- 파이썬 메서드 sum이 이 방법으로 만들어져 있음

---

## 11. 🔄 재귀 함수 (Recursive Function)

함수가 자기 자신을 내부에서 다시 호출하는 형태입니다. 코드가 단순해지고 가독성이 좋아지지만, 호출 시마다 스택 메모리를 사용하므로 메모리 부담이 커집니다.

### 1. 피보나치 수열 구현 (비재귀 - 반복문)

반복문을 사용하여 메모리 효율을 높인 방식입니다.

```python
def fibonacci(n:int) -> int:
    result = 1
    first = 1
    second = 1
    for _ in range(3, n+1):
        result = first + second
        second = first
        first = result
    return result

print(fibonacci(10))  # 55
print(fibonacci(30))  # 832040
```

### 2. 피보나치 수열 구현 (재귀)

수학적 정의를 그대로 코드로 옮겨 단순하지만, n이 커질수록 계산량이 기하급수적으로 늘어납니다.

```python
def fibonacci(n:int) -> int:
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(10))
# print(fibonacci(100)) # ⚠️ 주의: 스택 오버플로우 및 시간 초과 발생 가능
```

> Note: 재귀는 코드 상 단순해 보이지만, 매 호출마다 스택(Stack) 프레임을 생성하기 때문에 실행 시간이 오래 걸리고 메모리 점유율이 높습니다.
> 

---

## 12. 🎫pass 키워드

함수나 클래스를 선언할 때, 내부 구현을 나중에 하기 위해 비워두는 용도로 사용합니다.

- **목적:** 이름만 미리 만들어두고 구조를 잡을 때 사용

```python
def temp():
    pass
```

---

## 13. 함수를 변수에 저장 (First-class Function)

함수를 일반 변수처럼 할당하여 사용하는 개념입니다.

```python
def print_something(a):
    print(a)

p = print_something
p(123)
```

- **이점:** 도메인을 고정하고 IP 주소를 바꾸듯, 실제 구현부를 추상화된 별명(`p`) 뒤에 숨길 수 있어 **유지보수**에 유리합니다.
- **사례:** **도커(Docker)**나 **쿠버네티스(Kubernetes)**가 내부적으로 서비스를 배포할 때 계속해서 별칭(Alias/Label)을 만들어 관리하는 원리와 유사합니다.

---

## 14. 람다 (lambda)

- 이름이 없는 **한 줄짜리 익명 함수**입니다.
- *학습 팁:* 클라우드 분야를 깊게 파려면 너무 남발하지 않는 것이 좋습니다 (가독성 및 디버깅 이슈).

---

## 15. 함수형 프로그래밍 도구 (map, filter, reduce)

컨테이너(리스트 등) 데이터를 처리할 때 가장 많이 사용하는 삼총사입니다.

| **함수** | **역할** | **특징** |
| --- | --- | --- |
| **map** | 순회하며 연산 | 모든 요소에 함수를 적용해 결과(Iterator) 리턴 |
| **filter** | 골라내기 | 조건이 참인 데이터만 추출 |
| **reduce** | 누적 계산 | 모든 요소를 연산하여 하나의 최종값 생성 |
- **MapReduce:** 큰 데이터를 작은 부분으로 나누어 작업(Map)한 뒤 다시 합치는(Reduce) 개념으로 확장됩니다.

---

## 16. 변수 범위 및 클로저 (Scope & Closure)

### 1. 변수 범위 키워드

- **`global`**: 함수 내부에서 함수 외부에 선언된 변수를 수정하고 싶을 때 사용합니다.
- **`nonlocal`**: 중첩 함수 내에서, 자신을 감싸고 있는 외부 함수의 변수를 수정하고 싶을 때 사용합니다.

### 2. 클로저 (Closure)

- **정의**: 함수 내부에 또 다른 함수를 리턴하는 형태입니다.
- **특징**: 외부 함수의 실행이 끝나더라도 내부 함수가 외부 함수의 지역 변수 값을 기억하고 계속 사용할 수 있게 해줍니다.

---

## 17. 관점 지향 프로그래밍 (AOP)

> 핵심 개념: 비즈니스 로직(Business Logic)과 공통 관심사(Common Concern)를 분리하는 것
> 
- **문제점**: 함수, 클래스, 앱을 만들 때 비즈니스 로직과 공통 관심사가 섞여 있으면 유지보수가 어렵습니다.
- **해결책**: 이를 분리하여 관리하되, 실행 시점에는 함께 동작하도록 엮어주는 것이 AOP의 핵심입니다.
- **참고**: Java의 **Spring 프레임워크**가 이 설정을 가장 잘 처리하는 것으로 알려져 있습니다.

---

## 18. 데코레이터 (Decorator)

### 1. 개요

- Java의 **Annotation(`@`)**과 유사한 역할입니다.
- 다른 함수를 인수로 받아 어떤 처리를 수행하고 함수를 리턴하거나, 함수를 다른 함수나 객체로 대체합니다.
- **장점**: 함수를 수정하지 않고도 기능을 추가(함수 시작/끝 출력 등)할 수 있습니다.

### 2. 동작 원리

`@decorate`를 사용하면 내부적으로 다음과 같이 치환되어 동작합니다.

```python
# Decorator 적용
@decorate
def target():
    print('running target()')

# 위 코드는 아래와 동일하게 동작함
target = decorate(target)
```

### 3. 실습 예제

### ✅ 기본 데코레이터 구조

```python
# common concern (공통 관심사)
def deco(func):
    def inner():
        print("running inner")
    return inner

@deco
# business logic (비즈니스 로직)
def target():
    pass

target() # deco가 리턴하는 inner 함수가 호출됨
```

### ✅ 실행 시간 측정 데코레이터 (Clock)

```python
import time

def clock(func):
    def clocked(*args):
        t0 = time.time() # 시작 시간
        
        # 실제 함수(business logic) 수행
        result = func(*args)
        
        elapsed = time.time() - t0 # 소요 시간 계산
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

print('6! = ', factorial(6))`
```

---

## 19. 시스템 모니터링 및 로깅

비즈니스 로직에만 집중하기 위해 공통 관심사(모니터링, 로깅)는 외부 솔루션을 활용합니다.

### 1. 모니터링 및 시각화

- **Prometheus**: 메트릭(성능 데이터) 수집 및 저장
- **Grafana**: 수집된 데이터를 시각화 대시보드로 제공

### 2. 로깅 및 검색 (ELK / EFK Stack)

- **Elasticsearch**: 로그 데이터 검색 및 엔진
- **Logstash / Fluentd**: 로그 수집 및 저장소 전달
- **Kibana**: 로그 시각화 및 분석 도구

> 결론: 애플리케이션 코드에는 순수하게 비즈니스 로직만 작성하는 것을 지향해야 합니다.
> 

---