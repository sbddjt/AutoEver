import asyncio
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie
from pydantic import Field

# 1. 문서 모델 정의 (Pydantic 기반)
# Beanie의 Document를 상속받아 비동기 모델을 정의합니다.
class Product(Document):
    name: str
    price: float
    category: str
    description: Optional[str] = None
    
    class Settings:
        name = "products" # MongoDB 컬렉션 이름 지정

async def run_example():
    # 2. MongoDB 클라이언트 생성 및 연결
    # 비동기 드라이버인 Motor를 사용합니다.
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.test_database

    # 3. Beanie 초기화 (모델 등록)
    # 사용할 DB와 문서 모델 리스트를 등록합니다.
    await init_beanie(database=db, document_models=[Product])

    # --- [C] 데이터 생성 ---
    # 객체 생성 후 insert() 메서드를 비동기(await)로 호출합니다.
    new_product = Product(name="Gaming Mouse", price=45000, category="Electronics")
    await new_product.insert()
    print(f"생성된 상품 ID: {new_product.id}")

    # --- [R] 데이터 조회 ---
    # find_one()과 조건을 사용하여 데이터를 조회합니다.
    product = await Product.find_one(Product.name == "Gaming Mouse")
    if product:
        print(f"조회된 가격: {product.price}")

    # --- [U] 데이터 수정 ---
    # set() 메서드를 사용하여 데이터를 수정합니다. (딕셔너리 형태)
    if product:
        await product.set({Product.price: 39000})
        print("가격이 업데이트되었습니다.")

    # --- [D] 데이터 삭제 ---
    # delete() 메서드로 해당 문서를 삭제합니다.
    await product.delete()
    print("상품이 삭제되었습니다.")

# 비동기 루프 실행
# 메인 진입점에서 이벤트 루프를 실행합니다.
if __name__ == "__main__":
    asyncio.run(run_example())
