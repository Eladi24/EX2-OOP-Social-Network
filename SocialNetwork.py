# Network class
# ToDo Singleton pattern
from User import User


class SocialNetwork:
    __instance = None

    def __new__(cls, name):
        # If an instance doesn't exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name):
        self.name = name
        self.users = {}
        self.logged_in_users = []
        print(f"The social network {self.name} was created!")

    def sign_up(self, user_name, password):
        if user_name in self.users:
            raise NameError("User is already signed up")

        if not (4 <= len(password) <= 8):
            raise ValueError("Illegal password, try again")

        user = User(user_name, password)
        self.users[user_name] = user
        return user

    def log_in(self, user_name, password):
        if user_name in self.users and self.users[user_name].password == password:
            if self.users[user_name].is_logged_in():
                raise RuntimeError(f"{user_name} is already logged in")
            else:
                self.users[user_name].online = True
                print(f"{user_name} connected")

    def log_out(self, user_name):
        if user_name in self.users and self.users[user_name].is_logged_in():
            self.users[user_name].online = False
            print(f"{user_name} disconnected")
        else:
            raise RuntimeError(f"{user_name} is already disconnected")

    def __str__(self):
        result = f"{self.name} social network:\n"
        for user_name, user in self.users.items():
            result += (f"User name: {user_name}, Number of posts: {len(user.posts)}, Number of followers: "
                       f"{len(user.followers)}\n")
        return result
