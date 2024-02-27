from abc import ABC, abstractmethod


class Sender(ABC):

    @abstractmethod
    def follow(self, other_user):
        pass

    @abstractmethod
    def unfollow(self, other_user):
        pass

    @abstractmethod
    def notify(self, post):
        pass


class Member(ABC):

    @abstractmethod
    def update(self, notification):
        pass
