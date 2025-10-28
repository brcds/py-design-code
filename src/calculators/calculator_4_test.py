from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate_average():
    mock_request = MockRequest(body={"numbers": [4, 8, 8, 4]})
    calculator_4 = Calculator4()
    response = calculator_4.calculate(mock_request)
    assert response == {'data': {'Calculator': 4, 'media': '6.00', 'numbers': [4, 8, 8, 4], 'Success': True}}

