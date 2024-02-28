# Abstracts Post class
# ToDO Factory pattern
from abc import ABC, abstractmethod


class Post(ABC):
    def __init__(self, user):
        self._user = user
        self._likes = []
        self._liked = 0
        self._comments = []

    def like(self, user):
        if not self._user.is_logged_in():
            raise ValueError("User not logged in")

        if user not in self._likes:
            self._likes.append(user)
            if user != self._user:
                notification = f"{user.get_user_name()} liked your post"
                self._user.update(notification)
                self._liked += 1
                print(f"notification to {self._user.get_user_name()}: {notification}")

    def comment(self, user, text: str):
        if not self._user.is_logged_in():
            raise PermissionError("User not logged in")

        self._comments.append((user, text))
        if self._user != user:
            notification = f"{user.get_user_name()} commented on your post"
            self._user.update(notification)
            print(f"notification to {self._user.get_user_name()}: {notification}: {text}")

    @abstractmethod
    def __str__(self):
        pass

    def get_user(self):
        return self._user
