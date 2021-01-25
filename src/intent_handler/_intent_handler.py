import alexa_response_builder as response_builder
from common.utils import parse_json, to_json_string, encode_base64, decode_base64
from songs_library import SongsLibrary
from requests import get as http_get
import config
import random

class IntentHandler():
    _intent_name: dict

    def __init__(self, songs_library: SongsLibrary):
        self._intent_name = {
            'AMAZON.StopIntent': self.stop,
            'PlaySongsWithSlots': self.play_songs,
            'AMAZON.NextIntent': self.next,
            'AMAZON.PreviousIntent': self.previous,
            'AMAZON.PauseIntent': self.pause,
            'AMAZON.ResumeIntent': self.resume,
            'SeekForward': self.resume
        }
        self._queue = None

    def handle(self, event):
        try:
            return self._intent_name[event['request']['intent']['name']](event)
        except Exception as ex:
            print(ex)
            return response_builder.build_response(response_builder.build_speechlet_response("I couldn't understand this."))

    def get_audio_name_and_url(self, id: str):
        res = http_get(config.FileDetailsUrl.format(id=id))
        res = res.text
        res = parse_json(res)
        return res['name'], res['url']
    
    def get_all_folders(self):
        res = http_get(config.SubFoldersUrl.format(id='0'))
        res = res.text
        res = parse_json(res)
        return res

    def play_all(self, event, id: str = '0'):
        res = http_get(config.FilesInFolder.format(id=id))
        res = res.text
        res = parse_json(res)
        songs_list = [x['id'] for x in res]
        random.shuffle(songs_list)
        self._queue = songs_list
        audio_name, audio_url = self.get_audio_name_and_url(songs_list[0])
        res = response_builder.build_response(response_builder.build_audio_speechlet_response(f'Playing: {audio_name}', audio_url, '0'))
        return res    

    def play_songs(self, event):
        try:
            folder_name = event['request']['intent']['slots']['folder_name']['value']
            folder_list = self.get_all_folders()
            for x in folder_list:
                if str.find(str.lower(x['name']), str.lower(folder_name)) >= 0:
                    return self.play_all(event, x['id'])
        except KeyError:
            return self.play_all(event)

    def previous(self, event):
        curr_index = int(event['context']['AudioPlayer']['token'])
        mod = len(self._queue)
        index = (curr_index - 1) % mod

        audio_name, audio_url = self.get_audio_name_and_url(self._queue[index])
        res = response_builder.build_response(response_builder.build_audio_response(audio_url, index))
        return res

    def next(self, event, play_behaviour = 'REPLACE_ALL'):
        curr_index = int(event['context']['AudioPlayer']['token'])
        mod = len(self._queue)
        index = (int(curr_index) + 1) % mod

        audio_name, audio_url = self.get_audio_name_and_url(self._queue[index])
        res = response_builder.build_response(response_builder.build_audio_response(audio_url, index))
        return res

    def enqueue(self, event):
        curr_index = int(event['context']['AudioPlayer']['token'])
        mod = len(self._queue)
        index = (int(curr_index) + 1) % mod

        _, audio_url = self.get_audio_name_and_url(self._queue[index])
        res = response_builder.build_response(response_builder.build_enqueue_audio_response(audio_url, index, play_behaviour='REPLACE_ENQUEUED'))
        return res

    def resume(self, event):
        curr_index = int(event['context']['AudioPlayer']['token'])
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        audio_name, audio_url = self.get_audio_name_and_url(self._queue[curr_index])
        res = response_builder.build_response(response_builder.build_audio_speechlet_response(f'Resuming: {audio_name}', audio_url, curr_index, offsetInMilliseconds=offset))
        return res
    
    def pause(self, event):
        return response_builder.build_response(response_builder.build_stop_response())

    def stop(self, event: dict):
        return response_builder.build_response(response_builder.build_stop_response())