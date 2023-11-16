import re
from typing import Callable, Union

from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.decoder import decode_byte_to_dict
from app.utils.validators import validate_date, validate_email, validate_phone


class RequestBodyValidationMiddleware(BaseHTTPMiddleware):
    TYPES = {
        'date': validate_date,
        'phone': validate_phone,
        'email': validate_email,
    }

    async def set_body(
            self,
            request: Request,
    ) -> None:
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive

    async def dispatch(
            self,
            request: Request,
            call_next: Callable,
    ) -> JSONResponse:
        await self.set_body(request)

        errors = []
        body = await request.body()
        query = decode_byte_to_dict(body)

        for field_name, field_value in query.items():
            field_type = await self.__check_existing_name(field_name)
            if field_type:
                field_validator = self.TYPES.get(field_type)
                try:
                    field_validator(field_value)
                except ValueError as err:
                    errors.append(str(err))

        if errors:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content=errors,
            )
        return await call_next(request)

    async def __check_existing_name(self, value: str) -> Union[str, None]:
        data = re.split(r'[_ ,.]', value)
        return next((string for string in data if string in self.TYPES), None)
