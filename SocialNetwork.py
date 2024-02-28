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
        self.__name = name
        self.__users = {}
        print(f"The social network {self.__name} was created!")

    def sign_up(self, user_name, password):
        if user_name in self.__users:
            raise NameError("User is already signed up")

        if not (4 <= len(password) <= 8):
            raise ValueError("Illegal password, try again")

        user = User(user_name, password)
        self.__users[user_name] = user
        return user

    def log_in(self, user_name, password):
        if user_name in self.__users and self.__users[user_name].get_password(self) == password:

            if self.__users[user_name].is_logged_in():
                raise RuntimeError(f"{user_name} is already logged in")

            else:
                self.__users[user_name].set_logged_in(True)
                print(f"{user_name} connected")

        elif user_name in self.__users:
            raise PermissionError("Incorrect password")

        else:
            raise RuntimeError(f"{user_name} doesn't exist")

    def log_out(self, user_name):
        if user_name in self.__users:

            if self.__users[user_name].is_logged_in():
                self.__users[user_name].set_logged_in(False)
                print(f"{user_name} disconnected")

            else:
                raise RuntimeError(f"{user_name} is already disconnected")

        else:
            raise RuntimeError(f"{user_name} doesn't exist")

    def __str__(self):
        result = f"{self.__name} social network:\n"

        for user_name, user in self.__users.items():
            result += (f"User name: {user_name}, Number of posts: {user.get_posts_num()}, Number of followers: "
                       f"{user.get_followers_num()}\n")
        return result

