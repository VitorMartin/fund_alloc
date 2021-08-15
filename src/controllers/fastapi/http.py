from pydantic import Json

from src.controllers.fastapi.enums.status_code import STATUS_CODE


class HttpRequest:
    body: dict

    def __init__(self, body: dict):
        self.body = body


class HttpResponse:
    body: dict
    statusCode: int

    def __init__(self, body: dict, statusCode: STATUS_CODE = STATUS_CODE.OK):
        self.statusCode = statusCode.value
        self.body = body
