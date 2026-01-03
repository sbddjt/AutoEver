/*
    [Delete] 데이터 삭제
*/

// 1. remove (구버전)
// db.collection.remove(query)

// 2. deleteOne (조건에 맞는 1개 삭제)
db.users.deleteOne({ name: "test_user" });

// 3. deleteMany (조건에 맞는 다수 삭제)
db.users.deleteMany({ category: "temp_data" });