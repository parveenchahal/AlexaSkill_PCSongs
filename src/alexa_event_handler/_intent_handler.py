from .. import alexa_response_builder as response_builder

class IntentHandler():
    _intent_name: dict

    def __init__(self) -> None:
        self._intent_name = {
            'AMAZON.StopIntent': self.stop,
            'PlaySongsWithSlots': self.play_songs,
            'AMAZON.NextIntent': self.next,
            'AMAZON.PreviousIntent': self.previous,
            'AMAZON.PauseIntent': self.pause,
            'AMAZON.ResumeIntent': self.resume
        }

    def handle(self, event):
        try:
            return self._intent_name[event['request']['intent']['name']](event)
        except:
            return response_builder.build_response(response_builder.build_speechlet_response("I couldn't understand this."))

    def stop(self, event: dict):
        return response_builder.build_response(response_builder.build_stop_response())

    def play_songs(self, event):
        x = 'https://pchahal.blob.core.windows.net/songs/Cheerey%20Waalea.mp3'
        return response_builder.build_response(response_builder.build_speechlet_response('Playing: Cheerey Waalea', False))

    def next(self, event):
        x = 'https://pchahal.blob.core.windows.net/songs/Cheerey%20Waalea.mp3'
        return response_builder.build_response(response_builder.build_audio_speechlet_response('Playing next song: Cheerey Waalea', x, "Token", False))

    def previous(self, event):
        x = 'https://pchahal.blob.core.windows.net/songs/Cheerey%20Waalea.mp3'
        return response_builder.build_response(response_builder.build_speechlet_response('Playing previos song: Cheerey Waalea', False))

    def pause(self, event):
        return response_builder.build_response(response_builder.build_pause_response())

    def resume(self, event):
        return response_builder.build_response(response_builder.build_resume_response())
    