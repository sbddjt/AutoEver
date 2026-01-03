from pymongo import MongoClient

# 1. 클라이언트 연결
# MongoDB 기본 포트(27017)로 로컬호스트에 연결합니다.
conn = MongoClient('127.0.0.1')

# 2. 사용할 데이터베이스 설정
# 'seongyun'이라는 이름의 DB를 선택합니다. (없으면 데이터 입력 시 자동 생성)
db = conn.seongyun

# 3. 컬렉션 설정
# DB 내의 'users' 컬렉션을 선택합니다.
users = db.users

# 4. 데이터 생성 (JSON/Dict 형태)
doc1 = {'empno' : 1, 'name' : '해글러', 'sports': 'boxer'}
doc2 = {'empno' : 2, 'name' : '올라주원', 'sports': 'basketball'}
doc3 = {'empno' : 3, 'name' : '베르캄프', 'sports': 'soccer'}
doc4 = {'empno' : 4, 'name' : '차범근', 'sports': 'soccer'}
doc5 = {'empno' : 5, 'name' : '세필드', 'sports': 'baseball'}

# 5. 데이터 삽입
# insert_one: 단일 문서 삽입
users.insert_one(doc1)
users.insert_one(doc2)
users.insert_one(doc3)

# insert_many: 리스트 형태의 다중 문서 삽입
users.insert_many([doc4, doc5])

# 6. 데이터 조회 (Read)
# 전체 조회 - find()
# 반환된 Cursor 객체를 순회하며 데이터에 접근합니다.
result = users.find()
for r in result:
    print(r['name'])

# 조건 조회
# {'name': '차범근'} 조건에 맞는 문서를 찾습니다.
# result는 cursor 객체로 반환됩니다.
result = users.find({'name': '차범근'})
print(result)
# 출력 예시: <pymongo.synchronous.cursor.Cursor object at 0x00...>

# 7. 데이터 수정 (Update)
# update_one: 조건({'sports':'soccer'})에 맞는 문서 중 가장 먼저 발견된 하나만 수정
# $set 연산자를 사용하여 name 필드를 '크루이프'로 변경합니다.
users.update_one(
    {'sports':'soccer'},
    {
        '$set': {'name' : '크루이프'}
    }
)
