import logging
from flask import Flask
from flask_restful import Api
from controllers import EventController
from alexa_event_handler import AlexaEventHandler
from intent_handler import IntentHandler
from songs_library import SongsLibrary

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)

app = Flask(__name__)
api = Api(app)


alexa_event_handler = AlexaEventHandler(IntentHandler(SongsLibrary()))

api.add_resource(
    EventController,
    '/pc_songs/alexa_skill/event',
    endpoint="event_controller",
    resource_class_args=(logger, alexa_event_handler,))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)