from Post import Post


# SalePost class
class SalePost(Post):
    def __init__(self, user, item, price, location):
        super().__init__(user)
        self.item = item
        self.price = price
        self.location = location

    def print_post(self):
        pass

    def discount(self, reduction_num, password):
        pass

    def sold(self, password):
        pass