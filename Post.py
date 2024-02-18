# Abstracts Post class
# ToDO Factory pattern
from abc import ABC, abstractmethod


class Post(ABC):
    def __init__(self, user):
        self.user = user
        self.likes = []
        self.liked = 0
        self.comments = []

    def like(self, user):
        if user not in self.likes:
            self.likes.append(user)
            if user != self.user:
                notification = f"{user.user_name} liked your post"
                self.user.receive_notification(notification)
                self.liked += 1
                print(notification)

    def comment(self, user, text: str):
        self.comments.append((user, text))
        if self.user != user:
            notification = f"{user.user_name} commented on your post: {text}"
            self.user.receive_notification(notification)
            print(notification)

    @abstractmethod
    def __str__(self):
        pass
