/*
    [Update] 데이터 수정
    - replaceOne: 문서 전체 교체 (주의)
    - update/updateOne: 특정 필드만 수정
*/

// 1. replaceOne (통째로 교체)
// 주의: 지정하지 않은 필드는 모두 삭제됨
db.users.replaceOne(
    { name: "matt" },
    { name: "Karpoid", points: 101, password: "1111" }
);

// 2. update (부분 수정 - 권장)
// 연산자: $set, $inc, $unset, $currentDate
db.sample.update(
    { name: "park" },        // 조건
    { $set: { score: 100 } } // 변경 내용
);