from abc import ABC, abstractmethod


class AbstractBaseRepository(ABC):
    @abstractmethod
    async def fetch_all(self, *args, **kwargs):
        raise NotImplementedError
