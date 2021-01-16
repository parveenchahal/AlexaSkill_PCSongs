from abc import abstractclassmethod
class AbstractAlexaEventHandler(object):
    @abstractclassmethod
    def trigger(self, event: dict) -> dict:
        raise NotImplementedError()
    