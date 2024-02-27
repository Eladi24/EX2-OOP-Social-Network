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
        self.user_name = user_name
        self.password = password
        # Users that this user is following
        self.following = set()
        # Users that are following this user
        self.followers = set()
        self.posts = []
        self.online = True
        self.notifications = []

    def follow(self, other_user):
        if not self.online:
            # print("You must be logged in to follow a user")
            raise ValueError("User not logged in")
        self.following.add(other_user)
        other_user.followers.add(self)
        print(f"{self.user_name} started following {other_user.user_name}")

    def unfollow(self, other_user):
        if not self.online:
            # print("You must be logged in to unfollow a user")
            raise ValueError("User not logged in")

        self.following.remove(other_user)
        other_user.followers.remove(self)
        print(f"{self.user_name} unfollowed {other_user.user_name}")

    def publish_post(self, post_type, *args):
        if not self.online:
            # print("You must be logged in to publish a post")
            raise ValueError("User not logged in")
        post = PostFactory.factory(post_type, self, *args)
        self.posts.append(post)
        self.notify(post)
        print(post)
        return post

    def notify(self, post):
        for follower in self.followers:
            notification = f"{self.user_name} has a new post"
            follower.update(notification)

    def update(self, notification):
        # self.notifications.insert(0, notification)
        self.notifications.append(notification)

    def __str__(self):
        return (f"User name: {self.user_name}, Number of posts: {len(self.posts)}, "
                f"Number of followers: {len(self.followers)}")

    def print_notifications(self):
        print(f"{self.user_name}'s notifications:")
        for element in self.notifications:
            print(element)

    def is_logged_in(self):
        return self.online


