from urllib.parse import urlencode

import pytest
from fastapi.testclient import TestClient

from app.main import app
from tests.utils.json_data_reader import get_json_data


class TestFormFinder:
    test_data = get_json_data("testdata")

    @pytest.mark.parametrize(
        'test_request, expected_result, expected_status',
        [
            (test_data.get('request_1')),
            (test_data.get('request_3')),
            (test_data.get('request_3')),
            (test_data.get('invalid_request_1')),
            (test_data.get('invalid_request_2')),
        ],
    )
    async def test_get_form(self, test_request, expected_result, expected_status):
        with TestClient(app) as client:
            response = client.post(
                url='/api/v1/get_form',
                data=urlencode(test_request),
            )
            assert response.json() == expected_result
            assert response.status_code == expected_status
