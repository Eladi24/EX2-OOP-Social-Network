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
        if not self.user.online:
            raise ValueError("User not logged in")

        if user not in self.likes:
            self.likes.append(user)
            if user != self.user:
                notification = f"{user.user_name} liked your post"
                self.user.update(notification)
                self.liked += 1
                print(f"notification to {self.user.user_name}: {notification}")

    def comment(self, user, text: str):
        if not self.user.online:
            raise ValueError("User not logged in")

        self.comments.append((user, text))
        if self.user != user:
            notification = f"{user.user_name} commented on your post"
            self.user.update(notification)
            print(f"notification to {self.user.user_name}: {notification}: {text}")

    @abstractmethod
    def __str__(self):
        pass
