# 📂 3. CRUD (Create, Read, Update, Delete)

## 🔖 (참고) 기본 개념 및 환경

> Shading: 데이터 조각화, 수평 분할 (Scale-out)
> 
> 
> Clustering: 데이터 복제 및 그룹화
> 
> MEAN Stack: MongoDB, Express.js, Angular(→React), Node.js (모두 JavaScript 기반)
> 
- **언어 특징:** Python, JavaScript는 **동적 타이핑(Dynamic Typing)** 언어
- **유효성 검사 (Validation) & 보안 🛡️**
    - **Client:** 코드 노출 위험 있음. (보안 취약)
    - **Server:** 안전하지만 속도가 느림.
    - **원칙:** "네트워크를 믿지 마라(데이터 변질 가능성)." → 유효성 검사는 매 단계마다 수행해야 함.

---

## 0️⃣ JSON 데이터 표현

MongoDB는 BSON(Binary JSON)을 사용하지만 표기는 JSON 형식을 따릅니다.

- **객체 (Object):** `{ "키": "값", ... }`
- **배열 (Array):** `[ 값1, 값2, ... ]`
    - ⚠️ **주의:** MongoDB에서 **배열이 최상위(Root) 도큐먼트일 수는 없습니다.** (반드시 객체 `{}` 안에 포함되어야 함)

---

## 1️⃣ 데이터 전체 조회 (Simple Read)

가장 기본적인 컬렉션 데이터 조회 방법입니다.

```jsx
db.컬렉션이름.find()
```

---

## 2️⃣ 생성 (Create)

데이터를 데이터베이스에 추가하는 작업입니다.

### 💡 주요 특징

1. **원자성 (Atomicity):** 단일 도큐먼트 레벨에서 원자적으로 실행 (하나씩 순서대로 실행).
2. **_id 자동 생성:** 데이터를 삽입할 때 `_id` 키가 없으면 자동으로 생성되어 값이 추가됨.
3. **메서드 종류:** `insert`, `save`, `insertOne`, `insertMany`

### 🔹 insert vs save

- **insert:** 중복된 `_id` 삽입 시 **에러 발생**.
- **save:** 중복된 `_id` 삽입 시 **데이터 수정 (Upsert)**.

### 🔹 데이터 삽입 예시

**1. 단일 데이터 삽입**

```jsx
// 삽입 성공 시 성공 여부와 ObjectId 리턴
db.users.insert({ name: "adam", age: 25, gender: "man" })
```

**2. 중첩 데이터 (객체/배열) 삽입**

```jsx
db.inventory.insert({
    item: "ABC1",
    details: {
        model: "14Q3",
        manufacturer: "xyz Company"
    },
    stock: [
        { size: "s", qty: 25 },
        { size: "M", qty: 50 }
    ],
    category: "clothing"
})
```

**3. 배열 데이터의 처리**

- 배열 자체를 저장할 수는 없고, **분할해서 삽입**되거나 **속성 값**으로 들어가야 합니다.
- `db.users.insert([ {name:"matt"}, {name:"lara"} ])` → matt와 lara가 **각각 별도의 도큐먼트**로 저장됨.
- `db.users.insert([1, 2])` → 값 없이 id만 저장되는 문제 발생 가능 (`{key: value}` 형태 준수).

### ⚙️ 멀티 스레드 vs 싱글 스레드 (Ordered 옵션)

`insert` 함수의 두 번째 매개변수로 `ordered`를 설정할 수 있습니다.

- **`ordered: true` (기본값, 싱글 스레드):** 순서대로 삽입하다가 에러 발생 시 **중단**.
- **`ordered: false` (멀티 스레드):** 병렬 처리. 에러가 발생해도 나머지 작업 **계속 수행**.

```jsx
// 예시: unique 인덱스가 걸려있을 때 중복 데이터 삽입 시도
db.sample.createIndex({name: 1}, {unique: true}) // name 중복 불가 설정

// ordered: true (싱글) -> 에러 발생 시 이후 데이터(lee, choi) 저장 안 됨
db.sample.insert(
    [{name:"kim"}, {name:"park"}, {name:"lee"}, {name:"choi"}],
    {ordered: true}
)

// ordered: false (멀티) -> 에러 발생해도 나머지 데이터는 저장됨
db.sample.insert(
    [{name:"kim"}, {name:"park"}, {name:"lee"}, {name:"choi"}],
    {ordered: false}
)
```

### 🔑 ObjectId

- MongoDB의 고유 일련번호 (Primary Key 역할).
- **12byte 구성.**
- 직접 생성 시: `var newId = new ObjectId()`

### 🔹 insertOne & insertMany

- **insertOne:** 하나만 삽입. `WriteConcern`(Lock 설정) 매개변수 사용 가능.
    
    > WriteConcern? 데이터를 저장할 때 어디까지 확인하고 '성공' 처리할 것인가? (속도 vs 안전성). Kafka 등의 Message Broker가 이를 보완.
    > 
- **insertMany:** 여러 개 삽입. `BulkWriteError`를 통해 성공/실패 개수 확인 가능.

### 📝 자바스크립트 구문 활용

```jsx
var num = 1
for (var i = 0; i < 3; i++) {
    db.sample.insertOne({ name: "user"+i, score: num })
}
```

---

## 3️⃣ 읽기 (Read - Detailed)

데이터를 조건에 맞춰 조회합니다.

### 📌 기본 형식

```jsx
db.컬렉션이름.find(query, projection)
```

- `query`: 검색 조건 (SQL의 WHERE)
- `projection`: 조회할 필드 선택 (SQL의 SELECT)
- **반환값:** Cursor (도큐먼트를 조회할 수 있는 포인터)

### 📥 데이터 가져오기 (mongoimport)

JSON 파일을 DB로 가져올 때 사용합니다. (터미널/CMD에서 실행)

> Tip: Windows 사용 시 MongoDB Database Tools 설치 및 환경 변수(Path) 설정 필요.
> 

```bash
# 폴더 경로로 이동 후 실행
mongoimport -d 데이터베이스명 -c 컬렉션명 < 파일명.json

# 예시
mongoimport -d seongyun -c area < area.json
```

### 🔍 Filtering (조건 조회)

**1. 단순 일치**

```jsx
db.users.find({ name: "seongyun" })
```

**2. 비교 연산자**

- `$eq` (같음), `$ne` (다름)
- `$gt` (초과), `$gte` (이상), `$lt` (미만), `$lte` (이하)
- `$in` (포함), `$nin` (미포함)

```jsx
// item이 "hello"인 것
db.inventory.find({ item: { $eq: "hello" } })
// tags가 "blank" 또는 "blue"인 것
db.inventory.find({ tags: { $in: ["blank", "blue"] } })
```

### ⚠️ Null 조회와 $exists

MongoDB에서는 **속성이 없는 경우도 `null`로 간주**합니다.

```jsx
// y가 null이거나, y 필드 자체가 없는 도큐먼트 모두 검색됨
db.c.find({ y: null })

// 실제 값이 null이고 필드가 존재하는 경우만 검색하려면 $exists 사용
db.c.find({ z: { $eq: null, $exists: true } })
```

### 👁️ Projection (필드 선택)

- `1` (true): 조회함 / `0` (false): 조회 안 함
- **`_id` 필드는 명시적으로 `0`을 주지 않으면 무조건 조회됨.**

```jsx
// _id 제외, name만 조회
db.containerBox.find({}, { _id: false, name: true })
```

### 🔡 정규 표현식 (Regex)

```jsx
// 패턴: /pattern/옵션
// 옵션 - i:대소문자 무시, m:줄바꿈 무시(^사용시), x:공백 무시, s:dot(.)이 개행 포함

// 'a'가 포함된 데이터
db.users.find({ name: /a/ })
// 'pa'로 시작하는 데이터
db.users.find({ name: /^pa/ })
// 'ro'로 끝나는 데이터
db.users.find({ name: /ro$/ })
```

### 🎮 Cursor 제어 (Limit, Skip, Sort)

- **limit(n):** n개만 조회
- **skip(n):** n개 건너뛰고 조회
- **sort({필드: 1}):** 1(오름차순), -1(내림차순)
    - `$natural: 1` → 입력된 순서대로 정렬

```jsx
// id 기준 오름차순 정렬
db.users.find().sort({ id: 1 })
```

### 🔄 Cursor 메서드

커서(Cursor)는 데이터에 순차 접근하는 포인터(Iterator)입니다.

- **BOF:** Begin Of File (읽기 직전)
- **EOF:** End Of File (데이터 끝)

```jsx
var cursor = db.users.find()

// 많이 사용하는 패턴 (삼항 연산자)
cursor.hasNext() ? cursor.next() : null
```

---

## 4️⃣ 데이터 수정 (Update)

데이터 수정에는 크게 `replace` 방식과 `update` 방식이 있습니다.

### ⚠️ replaceOne (통째로 교체)

문서를 **새로운 내용으로 완전히 대체**합니다. 지정하지 않은 필드는 **삭제**되므로 주의해야 합니다.

```jsx
// name이 "matt"인 데이터를 찾아서 내용을 교체
// 주의: 기존에 있던 다른 필드(예: status)를 안 적으면 사라짐!
db.users.replaceOne(
    { name: "matt" },
    { name: "Karpoid", points: 101, password: "1111" }
)
```

### 🛠️ update / updateOne / updateMany (부분 수정)

연산자를 사용하여 **특정 필드만 수정**합니다. 안전하고 일반적인 방법입니다.

- **형식:** `update(조건, {연산자: {수정내용}}, 옵션)`
- **주요 수정 연산자:**
    - `$set`: 값 설정 (가장 많이 사용)
    - `$inc`: 값 증가
    - `$unset`: 필드 삭제
    - `$currentDate`: 현재 시간 입력

```jsx
// name이 "park"인 데이터의 score를 100으로 변경 (다른 필드 유지됨)
db.sample.update(
    { name: "park" },
    { $set: { score: 100 } }
)
```

---

## 5️⃣ 데이터 삭제 (Delete)

데이터를 컬렉션에서 제거합니다.

- `remove(query)`: (구버전) 조건에 맞는 데이터 삭제
- `deleteOne(query)`: 조건에 맞는 데이터 1개 삭제
- `deleteMany(query)`: 조건에 맞는 데이터 모두 삭제
