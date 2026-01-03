/*
    [Read] 데이터 조회
    - 문법: db.collection.find(query, projection)
*/

// ----------------------------------------------------
// 0. MongoImport (Terminal Command)
// mongoimport -d 데이터베이스명 -c 컬렉션명 < 파일명.json
// 예: mongoimport -d seongyun -c area < area.json
// ----------------------------------------------------

// 1. 기본 조회
db.users.find(); // 전체 조회
db.users.find({ name: "seongyun" }); // 단순 일치
db.containerBox.find({ category: "animal", name: "bear" }); // AND 조건

// 2. 비교 연산자
// $eq, $ne, $gt(초과), $gte(이상), $lt(미만), $lte(이하), $in, $nin
db.inventory.find({ item: { $eq: "hello" } });
db.inventory.find({ tags: { $in: ["blank", "blue"] } });

// 3. Null 조회 & $exists
// 잘못된 예: db.c.find({ z: null }) -> z가 없는 문서도 조회됨
// 올바른 예: 속성이 존재하면서($exists: true) 값이 null인 것
db.c.find({ z: { $eq: null, $exists: true } });

// 4. Projection (필드 선택)
// 1: 출력, 0: 미출력 (_id는 명시적 0 필수)
db.containerBox.find({}, { _id: false, name: true });

// 5. 정규 표현식 (Regex)
db.users.find({ name: /a/ });    // 'a' 포함
db.users.find({ name: /^pa/ });  // 'pa'로 시작
db.users.find({ name: /ro$/ });  // 'ro'로 끝남

/*
    🎮 Cursor Control (Limit, Skip, Sort)
    - 처리 순서: Sort -> Skip -> Limit
*/
db.users.find().limit(2);        // 2개만
db.users.find().skip(1);         // 1개 건너뛰고
db.users.find().sort({ id: 1 }); // 오름차순(1), 내림차순(-1)
db.users.find().sort({ $natural: 1 }); // 입력된 순서(Disk 저장 순서)

// Iterator 활용
var cursor = db.users.find();
cursor.hasNext() ? cursor.next() : null;