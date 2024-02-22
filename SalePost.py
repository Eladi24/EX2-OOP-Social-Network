from Post import Post


# SalePost class
class SalePost(Post):
    def __init__(self, user, item, price, location):
        super().__init__(user)
        self.item = item
        self.price = price
        self.location = location
        self.sale_status = True

    def __str__(self):
        if self.sale_status is True:
            return (f"{self.user.user_name} posted a product for sale:\n"
                    f"For sale! {self.item}, price: {self.price}, pickup from: {self.location}\n")
        else:
            return (f"{self.user.user_name} posted a product for sale:\n"
                    f"Sold! {self.item}, price: {self.price}, pickup from: {self.location}\n")

    def discount(self, reduction_num, password):
        self.price = self.price - (self.price * reduction_num)/100
        if password == self.user.password:
            print(f"Discount on {self.user.user_name} product! the new price is: {self.price}")

    def sold(self, password):
        if self.user.password == password:
            self.sale_status = False
            print(f"{self.user.user_name}'s product is sold")
