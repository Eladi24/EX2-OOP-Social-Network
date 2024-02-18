# User class
# ToDO Observer pattern
from Post import Post
from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


class User:
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
            print("You must be logged in to follow a user")
            return
        self.following.add(other_user)
        other_user.followers.add(self)
        print(f"{self.user_name} started following {other_user.user_name}")

    def unfollow(self, other_user):
        if not self.online:
            print("You must be logged in to unfollow a user")
            return

        self.following.remove(other_user)
        other_user.followers.remove(self)
        print(f"{self.user_name} unfollows {other_user.user_name}")

    def publish_post(self, post_type, *args):
        if not self.online:
            print("You must be logged in to publish a post")
            return
        if post_type == "Text":
            post = TextPost(self, *args)
        elif post_type == "Image":
            post = ImagePost(self, *args)
        elif post_type == "Sale":
            post = SalePost(self, *args)
        else:
            raise ValueError("Invalid post type")
        self.posts.append(post)
        self.notify_followers(post)
        print(post)
        return post

    def notify_followers(self, post):
        for follower in self.followers:
            notification = f"{self.user_name} has published a new post: {post}"
            follower.receive_notification(notification)

    def receive_notification(self, notification):
        self.notifications.insert(0, notification)

    def __str__(self):
        return (f"User name: {self.user_name}, Number of posts: {self.posts.__sizeof__()}, "
                f"Number of followers: {self.followers.__sizeof__()}")

    def print_notifications(self):
        print(f"{self.user_name}'s notifications:")
        for element in self.notifications:
            print(element)

    def is_logged_in(self):
        return self.online

