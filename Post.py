# Abstracts Post class
# ToDO Factory pattern
from abc import ABC, abstractmethod


class Post(ABC):
    def __init__(self, user):
        self.user = user
        self.likes = []
        self.comments = []

    def like(self, user):
        if user not in self.likes:
            self.likes.append(user)
            if user != self.user:
                notification = f"{user.user_name} liked your post: {self}"
                self.user.receive_notification(notification)

    def comment(self, user, text: str):
        self.comments.append((user, text))
        if self.user != user:
            notification = f"{user.user_name} commented on your post: {self}\n{text}"
            self.user.receive_notification(notification)

    @abstractmethod
    def print_post(self):
        pass
