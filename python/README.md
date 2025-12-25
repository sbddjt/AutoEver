# 🐍 Python Programming

> **Hyundai AutoEver Mobility SW Academy - Cloud Track** > 클라우드 네이티브 개발의 기초 언어인 Python의 핵심 문법부터 객체 지향 설계(OOP), 심화 기능까지 학습하고 정리하는 공간입니다.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
</div>

---

## 📖 Overview
클라우드 엔지니어링 및 백엔드 개발을 위한 **Fundamental Language**로서 Python을 심도 있게 학습합니다.
간결한 문법을 활용한 생산성 향상뿐만 아니라, **Pythonic Code(파이썬다운 코드)** 작성법, 메모리 관리 원리, 그리고 **객체 지향 프로그래밍(OOP)**을 통해 유지보수 가능한 소프트웨어 설계를 목표로 합니다.
학습한 내용은 향후 Django/FastAPI 프레임워크 활용 및 자동화 스크립트 작성의 기반이 됩니다.

## 🛠️ Environment
- **OS**: Windows 10/11 (or macOS)
- **Language**: Python 3.10+
- **IDE**: Visual Studio Code (Extensions: Pylance, Black Formatter)
- **VCS**: Git & GitHub
- **Virtual Env**: venv (Standard Library)

---

## 📅 Curriculum & Progress
현대오토에버 클라우드 트랙 커리큘럼에 맞춘 학습 진행 상황입니다.

### 1️⃣ Python Fundamentals & Flow Control
- [x] **Python 개요**: 인터프리터 언어의 특징, 가상환경(venv) 설정
- [x] **변수 및 자료형**: Number, String, Boolean, Type Conversion
- [x] **흐름 제어**: 조건문(if-elif-else), 반복문(for, while), `match-case`
- [x] **입출력(I/O)**: 표준 입출력, f-string 포맷팅

### 2️⃣ Data Structures & Functional Approach
- [ ] **컬렉션 프레임워크**: List, Tuple, Set, Dictionary 특징 및 성능 차이
- [ ] **Comprehension**: List/Dict Comprehension을 통한 효율적 데이터 생성
- [ ] **함수(Function)**: 매개변수(*args, **kwargs), Scope(global, nonlocal)
- [ ] **Lambda & Map/Filter**: 익명 함수와 고차 함수 활용

### 3️⃣ Object-Oriented Programming (OOP)
- [ ] **클래스와 인스턴스**: 생성자(`__init__`), `self`의 의미, 네임스페이스
- [ ] **캡슐화(Encapsulation)**: 접근 제어, `@property`, Getter/Setter
- [ ] **상속(Inheritance)**: 부모/자식 클래스, `super()`, 메소드 오버라이딩
- [ ] **다형성(Polymorphism)**: 매직 메소드(`__str__`, `__add__` 등) 오버로딩

### 4️⃣ Advanced Python (Deep Dive)
- [ ] **Module & Package**: `import` 동작 원리, `__init__.py`, 패키지 구조화
- [ ] **Exception Handling**: `try-except-else-finally`, 사용자 정의 예외
- [ ] **File I/O & Serialization**: Context Manager(`with`), JSON/Pickle 직렬화
- [ ] **Advanced Features**: Iterator, Generator(`yield`), Decorator(`@`), Closure

---

## 📝 Key Concepts Summary

### 🔍 Mutable vs Immutable
파이썬의 메모리 관리와 데이터 전달 방식을 이해하는 핵심 개념입니다.

| 분류 | 특징 | 해당 자료형 |
|:---:|:---|:---|
| **Immutable** | 생성 후 값 변경 불가. 변경 시 새로운 객체 생성 (Re-binding) | `int`, `float`, `str`, `tuple` |
| **Mutable** | 생성 후 값 변경 가능. 메모리 주소 유지 | `list`, `dict`, `set`, `bytearray` |

### 💡 Core Keyword Notes
- **Call by Object Reference**: 파이썬의 함수 인자 전달 방식(객체의 주소값을 전달하되, 불변/가변 여부에 따라 동작이 다름).
- **Generator**: `yield`를 사용하여 데이터를 한 번에 메모리에 올리지 않고, 필요할 때마다 생성하여 메모리 효율성을 높이는 방식.
- **Decorator**: 기존 함수를 수정하지 않고 기능을 확장(Wrapping)할 때 사용하는 디자인 패턴 (AOP 개념과 유사).
- **GIL (Global Interpreter Lock)**: 멀티 스레드 환경에서 하나의 스레드만 바이트코드를 실행하도록 제한하는 파이썬 인터프리터의 특징.

---

## 📂 Directory Structure
```bash
python/
├── 01_basics/          # 변수, 자료형, 제어문 기초
├── 02_data_struct/     # 리스트, 딕셔너리 등 자료구조 및 알고리즘
├── 03_functions/       # 함수, 람다, 스코프 규칙
├── 04_oop/             # 클래스, 상속, 다형성 예제
├── 05_modules/         # 모듈화 및 패키지 구조 실습
├── 06_advanced/        # 데코레이터, 제너레이터 등 심화 문법
└── assignments/        # 과제 및 미니 프로젝트 코드
