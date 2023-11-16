from datetime import datetime
from re import match

from email_validator import EmailNotValidError
from email_validator import validate_email as check_email


def validate_email(data: str) -> bool:
    try:
        check_email(data)
    except EmailNotValidError as e:
        raise ValueError(f'Invalid email format: {str(e)}')

    return True


def validate_date(date_string: str) -> bool:
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for date_format in date_formats:
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            pass
    raise ValueError("Invalid date format. It's need to be: %Y-%m-%d' or '%d.%m.%Y'")


def validate_phone(data: str) -> bool:
    if not match(
            pattern=r'^\+7(\s[0-9]{3}){2}(\s[0-9]{2}){2}',
            string=data,
    ):
        raise ValueError("Invalid phone number format. It's need to be: +7 xxx xxx xx xx")

    return True


def get_value_type(value: str) -> str:
    types = {
        'date': validate_date,
        'phone': validate_phone,
        'email': validate_email,
    }
    for field_type, field_validator in types.items():
        try:
            field_validator(value)
            return field_type
        except ValueError:
            pass
    else:
        return 'text'
