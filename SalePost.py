from Post import Post


# SalePost class
class SalePost(Post):
    def __init__(self, user, item, price, location):
        super().__init__(user)
        self.__item = item
        self.__price = price
        self.__location = location
        self.__sale_status = True

    def __str__(self):
        if self.__sale_status is True:
            return (f"{self._user.get_user_name()} posted a product for sale:\n"
                    f"For sale! {self.__item}, price: {self.__price}, pickup from: {self.__location}\n")
        else:
            return (f"{self._user.get_user_name()} posted a product for sale:\n"
                    f"Sold! {self.__item}, price: {self.__price}, pickup from: {self.__location}\n")

    def discount(self, reduction_num, password):
        if not self._user.is_logged_in():
            raise PermissionError("User not logged in")

        self.__price = self.__price - (self.__price * reduction_num) / 100

        if password == self._user.get_password(self):
            print(f"Discount on {self._user.get_user_name()} product! the new price is: {self.__price}")

        else:
            raise PermissionError("Incorrect password!")

    def sold(self, password):
        if not self._user.is_logged_in():
            raise PermissionError("User not logged in")

        if self._user.get_password(self) == password:
            self.__sale_status = False
            print(f"{self._user.get_user_name()}'s product is sold")

        else:
            raise PermissionError("Incorrect password!")
