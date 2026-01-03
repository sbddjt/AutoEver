from mongoengine import connect, Document, StringField, IntField, EmailField, DateTimeField
from datetime import datetime

# 1. 연결
# MongoDB 호스트와 포트, DB 이름을 지정하여 연결합니다.
connect(db="seongyun", host="localhost", port=27017)

# 2. 모델 설계 (Class 정의)
# Document를 상속받아 스키마를 정의합니다.
class User(Document):
    # 필드별 타입 및 제약조건(required, min_value 등) 설정
    name = StringField(required=True, max_length=50)
    age = IntField(min_value=0)
    email = EmailField(unique=True)
    created_at = DateTimeField(default=datetime.utcnow)

    # MongoDB 컬렉션 이름 지정
    meta = {
        "collection": "members"
    }

# 3. 데이터 생성 및 저장
# 객체 인스턴스를 생성하여 데이터를 준비합니다.
user = User(
    name='아이유',
    age=30,
    email='iu@example.com'
)
# user.save() 
# 주석 해제 시 실제 DB에 저장됩니다. (save 메서드 호출 필요)

# 4. 조회
# 전체 조회: User.objects()를 호출하여 모든 문서를 가져옵니다.
users = User.objects()
for user in users:
    print(user.name)

# 단건 조회
# 조건을 인자로 전달하고 .first()로 첫 번째 결과만 가져옵니다.
user = User.objects(name='아이유').first()
# 조회된 객체에서 .email 속성으로 바로 접근 가능합니다.
print(user.email)
