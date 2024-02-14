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
        self.following = []
        # Users that are following this user
        self.followers = []
        self.posts = []
        self.online = True
        self.notifications = []

    def follow(self, other_user):
        if not self.online:
            print("You must be logged in to follow a user")
            return
        if other_user not in self.following:
            self.following.append(other_user)
            other_user.followers.append(self)

    def unfollow(self, other_user):
        if not self.online:
            print("You must be logged in to unfollow a user")
            return
        if other_user in self.following:
            self.following.remove(other_user)
            other_user.followers.remove(self)

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
        return post

    def notify_followers(self, post):
        for follower in self.followers:
            notification = f"{self.user_name} has published a new post: {post}"
            follower.receive_notification(notification)

    def receive_notification(self, notification):
        self.notifications.insert(0, notification)

    def print_user(self):
        pass

    def print_notifications(self):
        print(f"{self.user_name}'s notifications:")
        for element in self.notifications:
            print(element)

    def is_logged_in(self):
        return self.online
