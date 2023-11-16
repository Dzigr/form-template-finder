from typing import Dict, Union

from fastapi import APIRouter, Request, status

from app.services.dependencies import Form_dep
from app.utils.decoder import decode_byte_to_dict

router = APIRouter(
    prefix='',
    tags=['Forms'],
)


@router.post(
    path='/get_form',
    status_code=status.HTTP_200_OK,
    summary='Get form',
)
async def get_form(
    request: Request,
    Form: Form_dep,
) -> Union[Dict[str, str], str]:
    body = await request.body()
    params = decode_byte_to_dict(body)
    return await Form.fetch_template(params)
