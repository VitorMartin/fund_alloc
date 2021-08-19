from src.controllers.fastapi.enums.status_code import STATUS_CODE


class HttpRequestBody:
    body: dict

    def __init__(self, body: dict):
        self.body = body


class HttpResponse:
    body: dict
    statusCode: int

    def __init__(self, body: dict, statusCode: int = STATUS_CODE.OK.value):
        self.statusCode = statusCode
        self.body = body
