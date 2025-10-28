from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def calculate(self, request: FlaskRequest) -> dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        media = self.__calculate_media(input_data)
        formated_response = self.__format_response(input_data, media)
        return formated_response

    def __validate_body(self, body: Dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado!")

        input_data = body["numbers"]

        if not isinstance(input_data, list):
            raise HttpBadRequestError("Informe uma lista de números!")

        if len(input_data) < 2:
            raise HttpBadRequestError("Informe pelo menos 2 números para calcular a média!")

        return input_data

    def __calculate_media(self, numbers: List[float]) -> float:
        sum_numbers = sum(numbers)
        len_numbers = len(numbers)
        media = sum_numbers / len_numbers
        return media

    def __format_response(self, numbers: list, media: float) -> Dict:
        media = "{:.2f}".format(media)
        return {"data": {"Calculator": 4, "media": media, "numbers": numbers, 'Success': True}}
