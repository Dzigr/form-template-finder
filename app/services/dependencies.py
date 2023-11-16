from typing import Annotated

from fastapi import Depends

from app.config import settings
from app.services.repository import AbstractBaseRepository, MongoMotorRepository
from app.services.services import FormService


def get_form_repo():
    form_repository = MongoMotorRepository(
        database_url=settings.db_url,
        database_name=settings.DB_NAME,

    )
    return FormService(form_repository)


Form_dep = Annotated[AbstractBaseRepository, Depends(get_form_repo)]
