from typing import Dict
from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 2.34, 2.14]})
    calculator_2 = Calculator2()
    calculator_2.calculate(mock_request)

    print()
    print(calculator_2)

