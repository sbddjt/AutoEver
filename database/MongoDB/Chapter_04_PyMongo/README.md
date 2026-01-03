# 🍃 4. Python & MongoDB 연동

## 💡 1. DB 연동의 기본 원리

> 왜 드라이버가 필요한가?
> 
> - **RDBMS (MariaDB 등):** SQL 인터페이스, 주로 **C++**로 작성됨
> - **NoSQL (MongoDB 등):** Javascript 인터페이스, **C++**로 작성됨
> - **Python:** 위 언어들과 사용 언어가 다름 ➡️ 이를 번역해서 전달해주는 **드라이버(Interface)**가 필요함
- **문제점:** 순수 드라이버만 쓰면 똑같은 코드 중복이 발생하고 개발 효율이 떨어짐.
- **해결책:** 개발자가 편하고 빠르게 함수 형태로 사용하기 위해 **ORM / ODM** 사용 (메모리 DB 형태)

---

## 🔌 2. 순수 드라이버 연동 (Pymongo)

가장 기본이 되는 방식입니다. `pip install pymongo` 명령어로 설치합니다.

### 2-1. 데이터 삽입 (Create)

```python
from pymongo import MongoClient

# 1. 클라이언트 연결
conn = MongoClient('127.0.0.1')

# 2. 사용할 데이터베이스 설정
db = conn.seongyun

# 3. 컬렉션 설정
users = db.users

# 4. 데이터 생성
doc1 = {'empno' : 1, 'name' : '해글러', 'sports': 'boxer'}
doc2 = {'empno' : 2, 'name' : '올라주원', 'sports': 'basketball'}
doc3 = {'empno' : 3, 'name' : '베르캄프', 'sports': 'soccer'}
doc4 = {'empno' : 4, 'name' : '차범근', 'sports': 'soccer'}
doc5 = {'empno' : 5, 'name' : '세필드', 'sports': 'baseball'}

# 5. 데이터 삽입
users.insert_one(doc1)
users.insert_one(doc2)
users.insert_one(doc3)
users.insert_many([doc4, doc5])
```

### 2-2. 데이터 조회 (Read)

```python
# 전체 조회 - find()
# 데이터를 순회하면 dict로 접근합니다.
result = users.find()
for r in result:
    print(r['name'])

# 조건 조회
# result는 cursor 객체로 반환됨
result = users.find({'name': '차범근'})
print(result)

# 출력 예시: <pymongo.synchronous.cursor.Cursor object at 0x00...>`
```

### 2-3. 데이터 수정 (Update)

```python
# 데이터 수정
# update_one: 가장 먼저 검색된 하나만 바뀜
# update_many: 조건에 맞는 모든 문서가 바뀜

users.update_one(
    {'sports':'soccer'},
    {
        '$set': {'name' : '크루이프'}
    }
)
```

---

## 🛠️ 3. ODM (Object Document Mapper) 연동

MongoDB와 같은 Document DB는 잘 사용하지 않는 추세지만, Python 객체처럼 다루기 위해 사용합니다.

### 3-1. ODM 개요 및 ORM과의 차이

> ODM이란?
> 
> - **O**bject **D**ocument **M**apper
> - JSON 형태의 문서를 Python의 **Class**처럼 다룰 수 있게 해주는 도구.
> - 딕셔너리 대신 객체를 이용한 작업 가능.
> - **종류:** `MongoEngine` (가장 많이 사용), `Beanie` (FastAPI와 호환성 좋음, 비동기)

| **구분** | **ODM (Object Document Mapper)** | **ORM (Object Relational Mapper)** |
| --- | --- | --- |
| **대상 DB** | MongoDB (문서형 DB) | MariaDB, MySQL (RDBMS) |
| **데이터 구조** | JSON / Document | Table / Row |
| **Python 패키지** | MongoEngine, Beanie | SQLAlchemy, Django ORM |

### 3-2. MongoEngine 사용 (동기)

`pip install mongoengine`

```python
from mongoengine import connect, Document, StringField, IntField, EmailField, DateTimeField
from datetime import datetime

# 1. 연결
connect(db="seongyun", host="localhost", port=27017)

# 2. 모델 설계 (Class 정의)
class User(Document):
    name = StringField(required=True, max_length=50)
    age = IntField(min_value=0)
    email = EmailField(unique=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        "collection": "members"
    }

# 3. 데이터 생성 및 저장
user = User(
    name='아이유',
    age=30,
    email='iu@example.com'
)
# user.save()

# 4. 조회
# 전체 조회
users = User.objects()
for user in users:
    print(user.name)

# 단건 조회
user = User.objects(name='아이유').first()
print(user.email)
```

---

## ⚡ 4. Beanie 사용 (비동기 ODM)

`pip install beanie motor`

- **특징:** 비동기(Async) ODM, `Motor`(드라이버) + `Pydantic`(검증) 기반

```python
import asyncio
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie
from pydantic import Field

# 1. 문서 모델 정의 (Pydantic 기반)
class Product(Document):
    name: str
    price: float
    category: str
    description: Optional[str] = None
    
    class Settings:
        name = "products" # MongoDB 컬렉션 이름 지정

async def run_example():
    # 2. MongoDB 클라이언트 생성 및 연결
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.test_database

    # 3. Beanie 초기화 (모델 등록)
    await init_beanie(database=db, document_models=[Product])

    # --- [C] 데이터 생성 ---
    new_product = Product(name="Gaming Mouse", price=45000, category="Electronics")
    await new_product.insert()
    print(f"생성된 상품 ID: {new_product.id}")

    # --- [R] 데이터 조회 ---
    product = await Product.find_one(Product.name == "Gaming Mouse")
    if product:
        print(f"조회된 가격: {product.price}")

    # --- [U] 데이터 수정 ---
    if product:
        await product.set({Product.price: 39000})
        print("가격이 업데이트되었습니다.")

    # --- [D] 데이터 삭제 ---
    await product.delete()
    print("상품이 삭제되었습니다.")

# 비동기 루프 실행
if __name__ == "__main__":
    asyncio.run(run_example())`
```

---

## ⚖️ 5. 핵심 정리 & Tip

- **ORM vs ODM 구분?**
    - **SQL(RDBMS):** `SELECT` 절을 사용하여 데이터를 가져옴 (ORM)
    - **NoSQL(MongoDB):** `find()` 등을 사용하며 스키마가 유연함 (ODM)
- **연결 관리 (Connection):**
    - **순수 드라이버:** 개발자가 직접 `open`하고 `close()`를 관리해야 함.
    - **ORM/ODM:** 내부적으로 연결을 관리해주며, **Connection Pool**을 사용하여 효율적으로 연결을 재사용함.

---
