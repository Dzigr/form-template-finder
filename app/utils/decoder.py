from typing import Dict
from urllib.parse import parse_qsl


def decode_byte_to_dict(byte_string: bytes) -> Dict[str, str]:
    return dict(parse_qsl(byte_string.decode()))
