from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_TYPE: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    SECRET_KEY: str

    @property
    def db_url(self):
        return (f'{self.DB_TYPE}://{self.DB_USER}:{self.DB_PASSWORD}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?authSource=admin')


settings = Settings()
