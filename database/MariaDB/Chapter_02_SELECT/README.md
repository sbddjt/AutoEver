# 📊[DB] MariaDB SELECT 문 기초 및 실습

## 1. SQL 실습 핵심 TIP 💡

- **효율적인 조건 필터링:** 성능 최적화를 위해 가능한 `WHERE` 절에서 먼저 데이터를 걸러내야 합니다. (`HAVING`은 그룹화 이후 필터링)
- **대소문자 구분:** `SELECT`, `FROM` 같은 예약어는 대소문자를 구분하지 않습니다.
- **데이터 구분:** MariaDB/MySQL은 기본적으로 `WHERE` 내 데이터 값의 대소문자를 구분하지 않으나, 필요 시 `BINARY` 설정을 통해 구분 가능합니다.
- **비절차적 언어:** SQL은 작성 순서대로 실행되지 않습니다. 
(**실행 순서: FROM → WHERE → SELECT**를 항상 유념!)
- **메모장 선작성 습관:** 사고 방지와 기록 관리를 위해 **메모장에 먼저 쿼리를 쓰고** 검토 후 DBMS에 옮겨 실행합니다. 📝
- **데이터의 가치:** 인프라는 복구 가능해도 **데이터는 유실되면 끝**입니다. 항상 신중하게 다뤄야 합니다. 💎

---

## 2. SELECT의 기본 형식과 데이터 조회 ⚙️

조회를 위한 가장 기본적인 SQL 구문이며, 테이블에서 원하는 컬럼을 선택해 가져옵니다.

### 1) 구문 형식

```sql
SELECT     [DISTINCT] * 또는 {컬럼이름 [별명]}  -- 조회할 컬럼
FROM       테이블이름 [새로운 이름]            -- 대상 테이블
[WHERE]    조건식                             -- 행 필터링
[GROUP BY] 그룹핑할 컬럼                       -- 데이터 그룹화
[HAVING]   그룹핑 후 조건                      -- 그룹 조건
[ORDER BY] 정렬할 컬럼 [ASC | DESC]           -- 결과 정렬
[LIMIT]    행 개수 [OFFSET 시작위치]           -- 출력 제한
```

### 2) 전체 및 특정 컬럼 조회 실습 💻

```sql
-- ① 테이블의 모든 컬럼을 조회할 때는 * 사용
SELECT *
FROM tCity;

-- ② 특정 컬럼(도시이름, 인구)만 나열하여 조회
SELECT name, popu
FROM tCity;

-- ③ 특정 컬럼(이름, 부서, 직급)만 조회
SELECT name, depart, grade
FROM tStaff;
```

---

## 3. SQL 실행 순서와 별명(Alias)의 관계 ⭐

쿼리는 작성 순서가 아닌 내부적인 절차에 따라 실행됩니다.

이 순서를 알아야 별명(Alias)의 사용 범위를 이해할 수 있습니다.

### 1) 실행 순서 (중요)

**FROM** ➔ **WHERE** ➔ **GROUP BY** ➔ **HAVING** ➔ **SELECT** ➔ **ORDER BY** ➔ **LIMIT**

### 2) SELECT 절에서의 별명(Alias) 활용

- **특징:** 결과 화면에 표시될 컬럼명을 변경할 수 있습니다.
    
    (`컬럼명 [AS] "별명"`)
    
- **주의:** 별명에 공백/특수문자가 있으면 **큰따옴표(" ")**가 필수입니다.
- **제약:** 별명은 **SELECT 단계 이후**에만 인식되므로, 이전 단계인 **WHERE 절에서는 사용할 수 없습니다.**

```sql
-- ✅ 올바른 별명 사용 (공백이 있으면 " " 필수)
SELECT name AS "도시 명"
FROM tCity;

-- ❌ 실행 순서에 따른 별명 오류 케이스
SELECT name AS "도시명"
FROM tCity
WHERE "도시명" = '부산';
-- 오류 발생 이유: WHERE 단계는 SELECT(별명 부여)보다
-- 먼저 실행되므로 '도시명'을 찾지 못함
```

---

## 4. 연산식 출력 및 별명 활용 🔢

컬럼 이름 대신 산술 연산(+, -, *, /, %)을 수행한 결과를 조회할 수 있습니다.

### 1) 연산식 실습

연산 결과의 컬럼명은 복잡해지기 때문에 가독성을 위해 반드시 **별명(Alias)**을 함께 사용하는 것이 좋습니다.

```sql
-- tCity 테이블에서 인구수(popu)에 10,000을 곱해 '인구'라는 별명으로 조회
SELECT name, popu * 10000 AS "인구"
FROM tCity;

-- 단순 계산식 출력
SELECT 24 * 365;
```

---

## 5. 컬럼 연결 조회 (CONCAT) 🔗

`CONCAT()` 함수를 사용하여 컬럼 이름이나 문자열을 합쳐서 출력할 수 있습니다.

```sql
-- EMP 테이블에서 이름과 직무를 문장으로 연결
SELECT CONCAT(ENAME, " 님의 직무는 ", JOB) AS "직무 안내"
FROM EMP;
```

---

## 6. DISTINCT (중복 제거) 🚫

`SELECT` 절에 한 번만 사용 가능합니다.

컬럼이 2개 이상이면 모든 컬럼의 값이 일치하는 경우만 제거됩니다.

```sql
-- ① region 중복 제거
SELECT DISTINCT region FROM tCity;
-- GROUP BY를 이용해서 중복을 제거
SELECT region FROM tCity GROUP BY region;

-- ② 두 컬럼 모두 같은 경우만 중복 제거
SELECT DISTINCT region, name FROM tCity;
```

---

## 7. 데이터 정렬 (ORDER BY) ↕️

데이터를 특정 기준에 따라 나열합니다. 

`ORDER BY` 절이 없으면 기본적으로 **기본키(Primary Key)** 순으로 조회됩니다.

- **ASC**: 오름차순 (기본값, 생략 가능)
- **DESC**: 내림차순
- **유연성**:
    - **Alias(별칭) 사용 가능**: `SELECT` 절에서 지정한 별명을 정렬 기준으로 쓸 수 있습니다.
    - **인덱스 번호**: 컬럼의 위치 번호로 정렬 가능하지만, 유지보수 측면에서 권장하지 않습니다.

```sql
-- ① 기본 정렬 (인구 오름차순)
SELECT * FROM tCity ORDER BY popu ASC;

-- ② 별칭 사용 가능 (ORDER BY는 SELECT 이후에 실행되므로 가능)
SELECT name, popu AS "인구수"
FROM tCity
ORDER BY 인구수 DESC;

-- ③ 인덱스 사용 (2번째 컬럼 기준 정렬)
SELECT name, popu 
FROM tCity 
ORDER BY 2 DESC;

-- ④ 정렬 기준에 없는 컬럼으로도 정렬은 가능하나 가독성을 위해 지양
SELECT name 
FROM tCity 
ORDER BY popu DESC;
```

---

## 8. WHERE 절 (조건 지정) 🔍

읽어올 레코드의 조건을 지정합니다. 

`SELECT` 뿐만 아니라 `UPDATE`, `DELETE` 시에도 대상을 특정하기 위해 필수적입니다.

- **기본 특징**: 생략 시 테이블의 모든 레코드를 대상으로 합니다.
- **리터럴 표기**: 문자열과 날짜는 반드시 **작은 따옴표(`'`)**로 감싸야 합니다.
- **대소문자 구분 (Collation) 접미사**:
    - **`_ci` (Case Insensitive)**: 대소문자 무시 (기본값).
    - **`_cs` (Case Sensitive)**: 대소문자 구분 (언어적 순서 유지).
    - **`_bin` (Binary)**: 대소문자 구분 (아스키/유니코드 **숫자값** 기준, 가장 빠름).

```sql
-- 1. 기본 조회 (작은 따옴표 필수)
SELECT * FROM tCity WHERE name = '서울';

-- 2. 대소문자 구분 (BINARY 키워드 사용)
SELECT * FROM tCity WHERE BINARY metro = 'y'; -- 'y'만 조회됨

-- 3. 컬럼 설정 변경 (Collation 수정)
ALTER TABLE tCity MODIFY metro VARCHAR(50) COLLATE utf8mb4_bin;
```

---

### (참고)

### 🌐 문자 집합 및 인코딩 (Encoding)

데이터 성격에 맞는 인코딩 선택은 클라우드 인프라 설계의 기초입니다.

| **인코딩 종류** | **특징** | **비고** |
| --- | --- | --- |
| **ASCII** | 영어/숫자/기호 표현 | 한글 표현 불가 |
| **MS949 (CP949)** | Windows 기본 한글 인코딩 | 하위 호환성 위주 |
| **EUC-KR** | 전통적인 한글 웹 인코딩 | 2Byte 한글 |
| **UTF-8** | 전 세계 문자 표현 (가변 3Byte) | 웹 표준 |
| **UTF-8mb4** | **4Byte** 기반 확장 UTF-8 | **이모지(Emoji)** 지원 (권장) |

---

## 🚫 NULL의 이해

### 1. 개념 정의

- **CS 관점**: 가리키는 데이터가 없음 (`nil`, `None`).
- **DB 관점**: **"아직 알려지지 않은 값" (Unknown)**.
- **Optional**: 현대 프로그래밍 언어(Swift, Kotlin 등)에서 NULL 가능성을 관리하는 방식과 유사합니다.

### 2. 내부 구현 원리 (Storage)🛠️

NULL은 단순히 0이나 공백이 아닙니다. 

- **Null Bitmap**: 데이터 레코드의 헤더 영역에 각 컬럼의 NULL 여부를 표시하는 비트(Flag)를 둡니다.
- **효율성**: 전체 데이터를 스캔하지 않고 헤더의 비트만 체크하여 NULL 여부를 즉시 판단하므로 연산 속도가 향상됩니다.

### 3. 조회 방법 (`IS NULL`)

NULL은 연산자(`=`, `<>`)로 비교할 수 없으며 전용 키워드 `IS NULL`, `IS NOT NULL` 를 사용해야 합니다.

```sql
-- score가 NULL인 데이터 조회
SELECT * FROM tStaff WHERE score IS NULL;

-- score가 존재하는 데이터 조회
SELECT * FROM tStaff WHERE score IS NOT NULL;
```

---

## ⚡ 논리 연산자 (AND, OR, NOT)

여러 조건을 결합할 때 사용하며, 연산 순서와 효율성을 고려해야 합니다.

### 1. 우선순위

> **NOT > AND > OR**
> 

복잡한 조건문에서는 가독성과 정확한 연산을 위해 **괄호`( )`** 사용을 강력히 권장합니다.

### 2. 성능 최적화 (Short-circuit Evaluation)

대용량 데이터 처리 시, 조건의 배치 순서가 성능에 영향을 미칩니다.

- **AND 연산**: **실패 확률이 높은(데이터를 많이 걸러낼 수 있는) 조건**을 앞에 배치합니다.
    - 앞의 조건이 `False`이면 뒤의 조건은 확인하지 않습니다.
- **OR 연산**: **성공 확률이 높은 조건**을 앞에 배치합니다.
    - 앞의 조건이 `True`이면 즉시 전체를 `True`로 판단합니다.
    
    ```sql
    -- 실무 예시: 4의 배수가 3의 배수보다 적으므로 앞에 두는 것이 효율적
    SELECT * 
    FROM numbers 
    WHERE num % 4 = 0 AND num % 3 = 0;
    ```
    

---

## 🧩LIKE 연산자 (패턴 검색)

`LIKE` 연산자는 정확한 일치가 아닌, **와일드카드**를 사용한 **부분 문자열 검색** 시 사용합니다.

### 1. 와일드카드 종류 🚩

- `%`: 글자 수 상관없음 (0글자 포함)
- `_`: 정확히 한 글자
- `[ ]`: 나열된 문자 중 하나
- `[^ ]`: 나열된 문자 제외
- **`ESCAPE`**: 와일드카드 문자 자체(`%`, `_`)를 검색해야 할 때 사용합니다.

---

### 2. `%`(글자 수 무제한) 활용 예제 🌊

`%`의 위치는 검색의 시작, 끝, 포함 여부를 결정합니다.

- **특정 문자 포함 검색** ('천'이 들어간 모든 이름)
    
    ```sql
    SELECT * 
    FROM tCity 
    WHERE name LIKE '%천%';
    ```
    
- **특정 문자로 시작하는 검색** ('천'으로 시작하는 이름)
    
    ```sql
    SELECT * 
    FROM tCity 
    WHERE name LIKE '천%';
    ```
    
- **날짜/연도 검색** (입사년도가 1981년인 데이터)
    - *주의: 데이터 타입이 문자열로 묵시적 형변환이 가능한 환경에서 사용 가능*
    
    ```sql
    SELECT * 
    FROM EMP 
    WHERE HIREDATE LIKE '1981%';
    ```
    

---

### 3. _ (정확한 위치/길이) 활용 예제 📍

`_`는 자릿수를 고정하여 정교하게 필터링할 때 유리합니다.

- **특정 위치의 글자 검색** (세 번째 글자가 '신'인 직원)
    
    ```sql
    - 앞에 두 글자(__)가 무엇이든 상관없고 세 번째가 '신'
    SELECT *
    FROM tStaff 
    WHERE name LIKE '__신%';
    ```
    
- **전체 글자 수 검색** (이름이 정확히 4글자인 직원)
    
    ```sql
    SELECT * 
    FROM tStaff 
    WHERE name LIKE '____';
    ```
    

---

### 4. ESCAPE 옵션 🛡️

데이터 내에 실제 와일드카드 문자인 `%`나 `_`가 포함되어 있을 때, 이를 일반 문자로 취급하여 검색하기 위해 사용합니다.

### ✅ 핵심 원리

- **`=` 연산자**: `WHERE sale = '30%'`라고 쓰면 정확히 '30%'라는 문자열과 일치하는 것만 찾습니다.
- **`LIKE` 연산자**: 패턴 검색을 수행하므로, `%`를 문자로 인식시키려면 **탈출(Escape) 문자**가 필요합니다.

**📝 실습 예제**

```sql
-- '#'을 탈출 문자로 지정하여 바로 뒤의 '%'를 일반 문자로 인식함
SELECT * 
FROM tTable 
WHERE sale LIKE '30#%' ESCAPE '#';
```

**💡 중요 포인트**

1. **자유도:** `ESCAPE`문자는 `#`, `!`, `$` 등 사용자가 **임의로 지정**할 수 있습니다. (데이터에 없는 특수문자 권장)
2. **작동 방식:** `ESCAPE`로 지정된 문자 **바로 다음에 오는 한 글자**는 와일드카드가 아닌 **일반 문자**로 취급됩니다.

---

## ↔️ BETWEEN 연산자 (범위 검색)

`A BETWEEN B AND C`는 특정 컬럼의 값이 **B 이상 C 이하**인 데이터를 조회할 때 사용합니다.

### ✅ 주요 특징

- **작성 순서 엄격**: 반드시 `BETWEEN [작은 값] AND [큰 값]` 순서로 작성해야 합니다.
    - ❌ `BETWEEN 100 AND 50` : 내부적으로 오름차순(Sort) 기반 검색을 수행하므로 결과가 나오지 않습니다.
- **성능적 우위**: `column >= 50 AND column <= 100` 처럼 컬럼 이름을 두 번 호출하는 것보다 `BETWEEN`이 내부 최적화 측면에서 더 효율적입니다.
- **확장성**: 숫자뿐만 아니라 **문자열**이나 **날짜** 데이터도 크기 비교가 가능합니다.

**📝 실습 예제**

```sql
-- ① 인구(popu)가 50에서 100 사이인 데이터 조회
SELECT * 
FROM tCity 
WHERE popu BETWEEN 50 AND 100;

-- ② 입사년도(hiredate)가 1981년인 데이터 조회
SELECT * 
FROM EMP 
WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31';
```

---

## 📋 IN 연산자 (목록 검색)

목록에 나열된 값 중 하나라도 일치하는 데이터를 조회합니다. 여러 개의 **`OR`** 조건을 결합한 것과 같습니다.

### ✅ 주요 특징

- **가독성**: 많은 양의 `OR` 조건을 나열하는 것보다 쿼리가 훨씬 간결해집니다.
- **가용성**: 나중에 서브쿼리(Subquery) 결과값들을 리스트로 받아올 때 매우 강력한 힘을 발휘합니다.

📝 **실습 예제**

```sql
-- region이 '경상' 또는 '전라'인 데이터 조회

-- OR 방식 (코드가 길고 지저분함)
SELECT * FROM tCity 
WHERE region = '경상' OR region = '전라';

-- IN 방식 (깔끔하고 직관적)
SELECT * FROM tCity 
WHERE region IN ('경상', '전라');
```

---

# 🛑 9. 행의 개수 제한 (LIMIT)

조회된 결과 집합의 행(Row) 개수를 제한할 때 사용합니다.

### ✅ 구문 형식 및 특징

- **위치**: 반드시 `SELECT` 구문의 **맨 마지막**에 작성합니다.
- **동작 시점**: 모든 정렬(`ORDER BY`)을 수행한 후에 잘라냅니다.
- **사용법**:
    1. `LIMIT [조회할 개수]`
    2. `LIMIT [조회할 개수] OFFSET [건너뛸 개수]`
    3. `LIMIT [건너뛸 개수], [조회할 개수]` (2번의 단축 표현)

**📝 실습 예제**

**① 상위 N개 데이터 조회**

`tCity` 테이블에서 면적(`area`)이 가장 큰 4개의 도시를 조회합니다.

```sql
SELECT *
FROM tCity
ORDER BY area DESC
LIMIT 4;
```

**② 페이징(Paging) 처리 (중간 데이터 조회)**

`tCity` 테이블에서 면적이 큰 순서대로 정렬 후, **3번째 데이터부터 3개**를 조회합니다. (앞의 2개는 건너뜀)

```sql
-- 방식 1: OFFSET 키워드 사용 (직관적)
SELECT *
FROM tCity
ORDER BY area DESC
LIMIT 3 OFFSET 2;

-- 방식 2: 쉼표(,) 사용 (앞 숫자가 건너뛸 개수)
SELECT *
FROM tCity
ORDER BY area DESC
LIMIT 2, 3;
```

**💡 Tip**: `LIMIT 2, 3`에서 앞의 `2`는 **Skip(건너뜀)**, 뒤의 `3`은 **Count(가져옴)**입니다.

---

# 💾 10. 검색 결과를 파일로 저장 (INTO OUTFILE)

`SELECT` 된 쿼리 결과를 서버 측의 파일로 저장합니다.

### ✅ **구문 형식**

```sql
SELECT ... 
INTO OUTFILE '파일경로'
  [CHARACTER SET 인코딩방식]
  [FIELDS 
      TERMINATED BY '구분자' 
      [OPTIONALLY] ENCLOSED BY '감싸는문자' 
      ESCAPED BY '탈출문자']
  [LINES 
      STARTING BY '시작문자' 
      TERMINATED BY '줄바꿈문자']
FROM ...
```

### ✅ 주요 옵션 설명

- **`OUTFILE '경로'`**: 쿼리 결과를 텍스트 파일로 저장합니다. 대신 변수명을 쓰면 변수에 저장됩니다.
- **`DUMPFILE`**: `BLOB` (이미지, 바이너리 등) 타입의 데이터를 저장할 때 `OUTFILE` 대신 사용합니다.
- **`FIELDS TERMINATED BY`**: 컬럼과 컬럼 사이를 구분할 문자 (보통 쉼표 `,`).
- **`ENCLOSED BY`**: 데이터 값을 감쌀 문자 (보통 따옴표 `"`).

**📝 실습 예제**

`members` 테이블의 모든 데이터를 CSV 형식처럼 만들어 지정된 경로에 저장합니다.

```sql
SELECT *
INTO OUTFILE 'C:\\Users\\USER\\Desktop\\sql파일.txt'
  FIELDS TERMINATED BY ','    -- 컬럼은 쉼표(,)로 구분
  ENCLOSED BY '"'             -- 데이터는 쌍따옴표(")로 감쌈
FROM members;
```

**⚠️ 주의**: 파일 경로는 OS에 따라 권한(Permission) 문제가 발생할 수 있으며, Windows 경로의 역슬래시(`\`)는 이스케이프 처리를 위해 두 번(`\\`) 써야 할 수 있습니다.
