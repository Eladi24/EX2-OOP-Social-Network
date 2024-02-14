from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# ImagePost class
class ImagePost(Post):
    def __init__(self, user, image_path):
        super().__init__(user)
        self.image_path = image_path

    def print_post(self):
        pass

    def display(self):
        # Read the image file
        img = mpimg.imread(self.image_path)

        # Display the image
        plt.imshow(img)
        plt.show()
