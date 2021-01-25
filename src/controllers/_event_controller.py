from flask_restful import request
from common import Controller
from common.utils import parse_json, to_json_string
from common.http_responses import Response
from alexa_event_handler import AbstractAlexaEventHandler

class EventController(Controller):
    event_handler: AbstractAlexaEventHandler

    def __init__(self, event_handler: AbstractAlexaEventHandler) -> None:
        self.event_handler = event_handler

    def post(self):
        res = self.event_handler.trigger(parse_json(request.data))
        return Response(to_json_string(res), 200, None, "application/json")
