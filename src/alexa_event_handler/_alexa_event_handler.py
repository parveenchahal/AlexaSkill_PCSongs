from ._alexa_abstract_event_handler import AbstractAlexaEventHandler
import alexa_response_builder as response_builder
from intent_handler import IntentHandler
from songs_library import SongsLibrary

class AlexaEventHandler(AbstractAlexaEventHandler):
    _request_type: dict
    _intent_handler: IntentHandler

    def __init__(self, intent_handler: IntentHandler):
        self._intent_handler = intent_handler
        self._request_type = {
            'LaunchRequest': self.launch_request,
            'SessionEndedRequest': self.empty_response,
            'IntentRequest': self.intent_request,
            'AudioPlayer.PlaybackStarted': self.empty_response,
            'AudioPlayer.PlaybackStopped': self.empty_response,
            'AudioPlayer.PlaybackNearlyFinished': self.enqueue,
            'AudioPlayer.PlaybackFinished': self.empty_response,
            'AudioPlayer.PlaybackFailed': self.empty_response
        }

    def trigger(self, event: dict) -> dict:
        try:
            return self._request_type[event['request']['type']](event)
        except KeyError:
            return response_builder.build_response(response_builder.build_speechlet_response("I couldn't understand this."))

    def launch_request(self, event: dict):
        return response_builder.build_response(response_builder.build_speechlet_response("What would you like to play. You can say play all.", False))
    
    def empty_response(self, event: dict):
        return response_builder.build_response(response_builder.build_empty_response())

    def intent_request(self, event):
        return self._intent_handler.handle(event)

    def enqueue(self, event):
        return self._intent_handler.enqueue(event)
