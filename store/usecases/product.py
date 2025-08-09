from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from store.core.schemas.product import ProductIn
from store.db.mongo import db_client


class ProductUsecase:
    def __init__(self, collection=None) -> None:
        if collection is None:
            client: AsyncIOMotorClient = db_client.get()
            database: AsyncIOMotorDatabase = client.get_database()
            self.collection = database.get_collection("products")
        else:
            self.collection = collection

    async def create(self, body: ProductIn):
        await self.collection.insert_one(body.model_dump())
