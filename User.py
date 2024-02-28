# User class
# ToDO Observer pattern
from Post import Post
from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost
from Observer import Sender, Member
from PostFactory import PostFactory


class User(Sender, Member):
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password
        # Users that this user is following
        self.__following = set()
        # Users that are following this user
        self.__followers = set()
        self.__posts = []
        self.__online = True
        self.__notifications = []

    def follow(self, other_user):
        if not self.__online:
            raise PermissionError("User not logged in")

        self.__following.add(other_user)
        other_user.add_follower(self)
        print(f"{self.__user_name} started following {other_user.get_user_name()}")

    def unfollow(self, other_user):
        if not self.__online:
            raise PermissionError("User not logged in")

        self.__following.remove(other_user)
        other_user.remove_follower(self)
        print(f"{self.__user_name} unfollowed {other_user.get_user_name()}")

    def publish_post(self, post_type, *args):
        if not self.__online:
            raise PermissionError("User not logged in")

        post = PostFactory.factory(post_type, self, *args)
        self.__posts.append(post)
        self.notify(post)
        print(post)
        return post

    def notify(self, post):
        for follower in self.__followers:
            notification = f"{self.__user_name} has a new post"
            follower.update(notification)

    def update(self, notification):
        self.__notifications.append(notification)

    def __str__(self):
        return (f"User name: {self.__user_name}, Number of posts: {len(self.__posts)}, "
                f"Number of followers: {len(self.__followers)}")

    def print_notifications(self):
        print(f"{self.__user_name}'s notifications:")
        for element in self.__notifications:
            print(element)

    def is_logged_in(self):
        return self.__online

    def get_user_name(self):
        return self.__user_name

    def get_followers_num(self):
        return len(self.__followers)

    def get_posts_num(self):
        return len(self.__posts)

    def set_logged_in(self, is_online):
        self.__online = is_online

    def add_follower(self, user):
        self.__followers.add(user)

    def remove_follower(self, user):
        self.__followers.remove(user)

    def get_password(self, instance):
        if isinstance(instance, User):
            raise PermissionError("This is private data!")

        else:
            return self.__password




