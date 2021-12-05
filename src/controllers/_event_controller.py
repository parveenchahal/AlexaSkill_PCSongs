from logging import Logger
import logging
from flask_restful import request
from common import Controller
from common.utils import parse_json, to_json_string, bytes_to_string
from common.http_responses import Response
from alexa_event_handler import AbstractAlexaEventHandler

class EventController(Controller):
    _logger: Logger
    _event_handler: AbstractAlexaEventHandler

    def __init__(self, logger: Logger, event_handler: AbstractAlexaEventHandler) -> None:
        self._logger = logger
        self._event_handler = event_handler

    def post(self):
        if request.data:
            str_data = bytes_to_string(request.data)
            self._logger.info(f'Request data: {str_data}')
        else:
            self._logger.info('request body is empty')
        res = self._event_handler.trigger(parse_json(request.data))
        return Response(to_json_string(res), 200, None, "application/json")
