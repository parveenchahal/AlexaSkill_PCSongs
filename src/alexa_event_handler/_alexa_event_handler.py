from ._alexa_abstract_event_handler import AbstractAlexaEventHandler
from .. import alexa_response_builder as response_builder
from ._intent_handler import IntentHandler

class AlexaEventHandler(AbstractAlexaEventHandler):
    _request_type: dict
    _intent_handler: IntentHandler

    def __init__(self):
        self._request_type = {
            'LaunchRequest': self.launch_request,
            'SessionEndedRequest': self.session_end_request,
            'IntentRequest': self.intent_request,
            'AudioPlayer': self.audio_player_request
        }
        self._intent_handler = IntentHandler()

    def trigger(self, event: dict) -> dict:
        try:
            return self._request_type[event['request']['type']](event)
        except KeyError:
            return response_builder.build_response(response_builder.build_speechlet_response("I couldn't understand this."))

    def launch_request(self, event: dict):
        return response_builder.build_response(response_builder.build_speechlet_response("Welcome to parveen songs. Say help if you need help", False))
    
    def session_end_request(self, event: dict):
        return {}

    def intent_request(self, event):
        return self._intent_handler.handle(event)

    def audio_player_request(self):
        pass