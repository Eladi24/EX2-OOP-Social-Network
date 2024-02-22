from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class PostFactory:
    @staticmethod
    def factory(post_type, user, *args):
        if post_type == "Text":
            post = TextPost(user, *args)
        elif post_type == "Image":
            post = ImagePost(user, *args)
        elif post_type == "Sale":
            post = SalePost(user, *args)
        else:
            raise ValueError("Invalid post type")
        return post
