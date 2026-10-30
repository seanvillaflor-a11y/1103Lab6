
class Product:
    def _init_(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price= price
        self._stock = stock

    def update_stock(self, quantity):
        if quantity >= 0:
            self._stock = quantity

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock