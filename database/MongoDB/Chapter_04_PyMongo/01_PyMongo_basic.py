"""
[순수 드라이버] Pymongo 연동
- 가장 기본이 되는 방식
- SQL처럼 데이터를 딕셔너리 형태로 직접 제어
"""

from pymongo import MongoClient

# 1. 클라이언트 연결
# 로컬 호스트 연결 (기본 포트: 27017)
conn = MongoClient('127.0.0.1', 27017)

# 2. 데이터베이스 설정 (없으면 자동 생성)
db = conn.seongyun

# 3. 컬렉션 설정
users = db.users

# --- [Create] 데이터 생성 ---
doc1 = {'empno': 1, 'name': '해글러', 'sports': 'boxer'}
doc2 = {'empno': 2, 'name': '올라주원', 'sports': 'basketball'}
doc3 = {'empno': 3, 'name': '베르캄프', 'sports': 'soccer'}
doc4 = {'empno': 4, 'name': '차범근', 'sports': 'soccer'}
doc5 = {'empno': 5, 'name': '세필드', 'sports': 'baseball'}

# 단건 삽입
users.insert_one(doc1)
users.insert_one(doc2)
users.insert_one(doc3)

# 다건 삽입
users.insert_many([doc4, doc5])


# --- [Read] 데이터 조회 ---
# 전체 조회 (Cursor 반환 -> 순회하며 출력)
all_users = users.find()
for r in all_users:
    print(f"Name: {r['name']}, Sports: {r['sports']}")

# 조건 조회
condition_user = users.find({'name': '차범근'})
for r in condition_user:
    print(f"Found: {r}")


# --- [Update] 데이터 수정 ---
# update_one: 조건에 맞는 첫 번째 문서만 수정
# update_many: 조건에 맞는 모든 문서 수정
users.update_one(
    {'sports': 'soccer'},  # 조건
    {'$set': {'name': '크루이프'}}  # 변경 내용
)

# 확인
updated_user = users.find_one({'name': '크루이프'})
print(f"Updated: {updated_user}")
