import json
from flask_restful import Resource, request, ResponseBase
from flask_restful import output_json
from ..alexa_event_handler import AbstractAlexaEventHandler

class EventController(Resource):
    event_handler: AbstractAlexaEventHandler

    def __init__(self, event_handler: AbstractAlexaEventHandler) -> None:
        self.event_handler = event_handler

    def post(self):
        res = self.event_handler.trigger(json.loads(request.data))
        return ResponseBase(json.dumps(res), 200, [], "application/json")