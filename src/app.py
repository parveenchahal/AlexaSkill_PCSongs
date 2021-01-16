from flask import Flask
from flask_restful import Api
from controllers import EventController
from alexa_event_handler import AlexaEventHandler

app = Flask(__name__)
api = Api(app)

alexa_event_handler = AlexaEventHandler()
api.add_resource(EventController, '/apis/event', endpoint="event_controller", resource_class_args=(alexa_event_handler,))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)