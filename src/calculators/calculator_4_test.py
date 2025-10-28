from .calculator_4 import Calculator4


def test_calculate_average():
    calculator_4 = Calculator4()
    response = calculator_4.calculate_average([4, 8, 8, 4])
    assert response == {'data': {'Calculator': 4, 'average': 6.0}}
