# Network class
# ToDo Singleton pattern
from User import User


class SocialNetwork:

    __instance = None

    def __new__(cls, **kwargs):
        # If an instance doesn't exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, kwargs)

        return cls.__instance

    def __init__(self, name):
        self.name = name
        self.users = []
        self.logged_in_users = []

    def sign_up(self, username, password):
        if any(user.user_name == username for user in self.users):
            print("Error: Username already in use.")
            return False
        if not (4 <= len(password) <= 8):
            print("Error: Password must be between 4 and 8 characters.")
            return False
        user = User(username, password)
        self.users.append(user)
        return user

    def log_in(self, user, password):
        if user.password == password and not user.is_logged_in():
            user.online = True

    def log_out(self, user):
        if user.is_logged_in():
            user.online = False

    def print(self):
        print(f"The social network {self.name} was created!")
