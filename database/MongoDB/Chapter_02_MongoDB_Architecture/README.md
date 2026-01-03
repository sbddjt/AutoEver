# 🍃 2. MongoDB Architecture & Work Units

## 1. 📂 작업 단위 (Work Units)

MongoDB의 작업 단위는 크게 **Database**와 **Collection**으로 나뉩니다.

### 1) Database

가장 큰 물리적 작업 단위입니다.

- **성능 영향:** 동시 처리 성능과 밀접하게 연관되어 있습니다.
- **Lock킹(Locking):** Collection이나 Index를 추가/변경하는 경우 **Database 수준의 Lock**이 적용됩니다.

### 🛠 관련 명령어 (Shell)

```jsx
// 1. 데이터베이스 목록 확인
show dbs
// -> 초기 상태: admin, config, local만 표시됨

// 2. 데이터베이스 사용 설정 (없으면 생성, 있으면 전환)
use seongyun 
// -> 'switched to db seongyun'

// 3. 현재 데이터베이스 확인
db

// 4. 데이터베이스 삭제
db.dropDatabase()
```

> ⚠️ 주의사항
> 
> - `use` 명령어로 데이터베이스를 생성해도, **실제 데이터를 삽입(Insert)하기 전까지는 목록(`show dbs`)에 나타나지 않습니다.**
> - **실습 예시:**JavaScript
> 
> ```jsx
> use seongyun                  // DB 생성
> db.mycollection.insertOne({name:1}) // 데이터 1개 추가
> show dbs                      // 이제 목록에 'seongyun'이 보임
> ```
> 

### 2) Collection

RDBMS의 Table과 유사한 **문서(Document)의 집합**입니다. 

### 🛠 관련 명령어

```jsx
// 1. 컬렉션 생성 (데이터 삽입 시 없으면 자동 생성됨)
db.createCollection('이름')

// 2. 현재 DB의 컬렉션 목록 확인
show collections

// 3. 컬렉션 이름 변경
db.oldName.renameCollection('newName')

// 4. 컬렉션 제거
db.collectionName.drop()
```

---

## 2. 🔄 Capped Collection (캡드 컬렉션)

크기가 고정된 컬렉션으로, **용량이 가득 차면 가장 오래된 데이터부터 자동으로 삭제**됩니다. 

### 💡 활용 분야

- **임베디드 환경:** 메모리 크기가 제한된 환경에서 유용.
- **로그(Log) 데이터:** 오래된 데이터는 필요 없고 최신 데이터만 유지해야 하는 경우.

### 💻 실습: 생성 및 동작 확인

**1. 생성 및 데이터 삽입**

```jsx
// 1. 사이즈가 10,000 바이트인 Capped Collection 생성
db.createCollection('cappedCollection', {capped:true, size:10000})

// 2. 데이터 1개 삽입 테스트
db.cappedCollection.insertOne({x:1})

// 3. for문을 이용한 대량 데이터 삽입 (JS 문법 사용 가능)
for (i = 0; i < 1000; i++) {
    db.cappedCollection.insertOne({x:i})
}
// -> MongoDB 셸이 JavaScript 기반임을 알 수 있음
```

**2. 결과 확인 및 상태 조회 (stats)**

db.cappedCollection.stats() 명령어로 상태를 조회했을 때의 예시입니다.

```jsx
{
  sharded: false,
  size: 9976,           // 현재 데이터 크기
  count: 344,           // 저장된 문서 개수 (1000개를 넣었으나 제한으로 인해 344개만 남음)
  numOrphanDocs: 0,
  storageSize: 40960,
  maxSize: 10000,       // 설정한 최대 크기
  ns: 'seongyun.cappedCollection',
  ...
}
```

> 📝 분석:
> 
> - `maxSize`를 10,000으로 설정했기 때문에, 1,000개의 데이터를 넣었음에도 불구하고 오래된 데이터는 삭제되고 **최신 데이터 약 344개(`count`)**만 남아있는 것을 확인할 수 있습니다.

---

## 3. ⚡️ BSON & Document 구조

MongoDB는 데이터를 **BSON(Binary JSON)** 형태로 저장하여 성능을 최적화합니다. 

### 📌 주요 특징

- **Light Weight:** 문자열뿐만 아니라 이진(Binary) 데이터 타입을 사용하여 저장 공간 절약 및 네트워크 전송 효율 증가.
- **Traversable:** 데이터 길이 정보가 포함되어 있어 필요한 필드만 빠르게 탐색 가능.
- **Efficient:** C언어의 Primitive 타입을 사용하여 인코딩/디코딩 속도가 빠름.

### 🔑 주요 데이터 타입 (Data Types)

| **타입** | **설명** | **예시** |
| --- | --- | --- |
| **ObjectId** | Primary Key(`_id`)로 사용. 12Byte (유닉스시간+기기ID+프로세스ID+카운터) | `ObjectId("...")` |
| **Date** | 64비트 정수(유닉스 시간) 저장 | `ISODate("...")` |
| **Timestamp** | 내부 복제 로그 등에 사용 (초 단위 + 순번) | `Timestamp(1412..., 1)` |
| **Array** | 배열 형태, 여러 문서 포함 가능 | `["a", "b"]` |

### ⚠️ Document 제약 사항

- 최대 크기: **16MB**
- 중첩 깊이: 최대 **100 Level**
- Key 제약: 중복 불가, `$` 및 `.` 문자 사용 불가, `null` 문자 포함 불가.
