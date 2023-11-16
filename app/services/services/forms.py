from typing import Dict, List

from app.services.repository import AbstractBaseRepository
from app.utils.validators import get_value_type


class FormService:
    def __init__(self, repository: AbstractBaseRepository) -> None:
        self.repo = repository

    async def fetch_template(self, data: Dict[str, str]) -> Dict[str, str]:
        query = await self.__prepare_query(data)
        template_name = await self.__match_data(query)

        return template_name if template_name else query

    async def __get_prepared_templates(self) -> List[Dict[str, str]]:
        templates = await self.repo.fetch_all()
        return [
            {
                'name': template.get('template_name'),
                'fields': {
                    (key, value) for key, value in template.items() if key != 'template_name'}
            } for template in templates
        ]

    async def __match_data(self, query: Dict[str, str]):
        query_set = {item for item in query.items()}
        templates_fields = await self.__get_prepared_templates()

        for template in templates_fields:
            if template.get('fields').issubset(query_set):
                return template['name']

    async def __prepare_query(self, query: Dict[str, str]) -> Dict[str, str]:
        return {key: get_value_type(value) for key, value in query.items()}
