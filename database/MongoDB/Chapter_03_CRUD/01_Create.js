/*
    [Create] 데이터 생성
    - 메서드: insert, save, insertOne, insertMany
    - 특징: _id 자동 생성, 원자성(Atomicity) 보장
*/

// 1. 단일 데이터 삽입
// 성공 시 WriteResult({ "nInserted": 1 }) 반환
db.users.insert({name : "adam", age : 25, gender : "man"});

// 2. 중첩 데이터 (Nested Object/Array)
db.inventory.insert({
    item: "ABC1",
    details: { model: "14Q3", manufacturer: "xyz Company" },
    stock: [
        { size: "s", qty: 25 },
        { size: "M", qty: 50 }
    ],
    category: "clothing"
});

// 3. 배열 데이터 처리 (주의)
// 배열 자체를 Root로 넣을 수 없음 -> 각 객체가 개별 문서로 저장됨
db.users.insert([{ name: "matt" }, { name: "lara" }]); 
// 잘못된 예: db.users.insert([1, 2]) -> 값만 저장 불가

// 4. insert vs save
// insert: 중복 _id 삽입 시 에러
// save: 중복 _id 삽입 시 덮어쓰기 (Upsert)

/*
    ⚙️ Ordered 옵션 (싱글 스레드 vs 멀티 스레드)
    - true (Default): 순서대로 실행, 에러 발생 시 중단
    - false: 병렬 실행, 에러 발생해도 나머지 작업 수행
*/
db.sample.createIndex({name: 1}, {unique: true}); // 중복 불가 설정

// ordered: false 예시
db.sample.insert(
    [{name:"kim"}, {name:"park"}, {name:"lee"}, {name:"choi"}],
    { ordered: false }
);

// 5. JavaScript Loop 활용
var num = 1;
for (var i = 0; i < 3; i++) {
    db.sample.insertOne({ name: "user"+i, score: num });
}