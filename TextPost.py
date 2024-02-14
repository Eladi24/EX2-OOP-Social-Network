from Post import Post


# TextPost class
class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)
        self.text = text

    def print_post(self):
        pass
