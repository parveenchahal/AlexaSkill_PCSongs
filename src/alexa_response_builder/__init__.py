def build_response(response: dict, session_attributes: dict = {}, version: str = '1.0'):
    return {
        'version': version,
        'sessionAttributes': session_attributes,
        'response': response
    }

def build_empty_response():
    return {
        'shouldEndSession': True
    }

def build_pause_response(output: str = ""):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'directives': [{
            'type': 'AudioPlayer.Stop'
        }],
        'shouldEndSession': True
    }

def build_stop_response(output: str = ""):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'directives': [{
            'type': 'AudioPlayer.Stop'
        }],
        'shouldEndSession': True
    }



def build_speechlet_response(output: str, should_end_session: bool = True):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'shouldEndSession': should_end_session
    }

def build_audio_response(url: str, token: str, should_end_session: bool = True, offsetInMilliseconds: int = 0, play_behaviour = 'REPLACE_ALL'):
    return {
        'directives': [{
            'type': 'AudioPlayer.Play',
            'playBehavior': play_behaviour,
            'audioItem': {
                'stream': {
                    'token': str(token),
                    'url': url,
                    'offsetInMilliseconds': offsetInMilliseconds
                }
            }
        }],
        'shouldEndSession': should_end_session
    }

def build_audio_speechlet_response(output: str, url: str, token: str, should_end_session: bool = True, offsetInMilliseconds: int = 0, play_behaviour = 'REPLACE_ALL'):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'directives': [{
            'type': 'AudioPlayer.Play',
            'playBehavior': play_behaviour,
            'audioItem': {
                'stream': {
                    'token': str(token),
                    'url': url,
                    'offsetInMilliseconds': offsetInMilliseconds
                }
            }
        }],
        'shouldEndSession': should_end_session
    }

def build_enqueue_audio_response(url: str, token: str, should_end_session: bool = True, offsetInMilliseconds: int = 0, play_behaviour = 'REPLACE_ALL'):
    return {
        'directives': [{
            'type': 'AudioPlayer.Play',
            'playBehavior': play_behaviour,
            'audioItem': {
                'stream': {
                    'token': str(token),
                    'url': url,
                    'offsetInMilliseconds': offsetInMilliseconds
                }
            }
        }],
        'shouldEndSession': should_end_session
    }