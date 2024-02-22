from Post import Post


# TextPost class
class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)
        self.text = text

    def __str__(self):
        return (f"{self.user.user_name} published a post:\n"
                f"\"{self.text}\"\n")
