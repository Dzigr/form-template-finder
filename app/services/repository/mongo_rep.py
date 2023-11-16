from typing import Dict, List, Union

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from .base import AbstractBaseRepository


class MongoMotorRepository(AbstractBaseRepository):
    def __init__(self, database_url: str, database_name: str) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(database_url)
        self.db: AsyncIOMotorCollection = self.client[database_name]

    async def fetch_all(self, limit: int = None) -> Union[List[Dict[str, str]], None]:
        async with await self.client.start_session() as session:
            return await self.db.templates.find(
                session=session,
                projection={"_id": 0},
            ).to_list(limit)
