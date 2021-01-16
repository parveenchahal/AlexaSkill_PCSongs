from flask_restful import request
from common import Controller
from common.utils import parse_json
from common.http_responses import JSONResponse
from alexa_event_handler import AbstractAlexaEventHandler

class EventController(Controller):
    event_handler: AbstractAlexaEventHandler

    def __init__(self, event_handler: AbstractAlexaEventHandler) -> None:
        self.event_handler = event_handler

    def post(self):
        res = self.event_handler.trigger(parse_json(request.data))
        return JSONResponse(res)