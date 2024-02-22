from abc import ABC


class Sender(ABC):

    def __init__(self):
        self._followers = set()

    def follow(self, user):
        pass

