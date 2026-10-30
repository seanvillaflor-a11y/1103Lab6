class Product:
    """Represents one product and manages its own state."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # ---- Read-only access (properties) ----
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    # ---- Behaviour ----
    def update_stock(self, quantity):
        """Set the stock to quantity. Rejects negative values."""
        if quantity < 0:
            print("Stock cannot be negative.")
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        print("ID: " + self.__product_id
              + " | Name: " + self.__name
              + " | Price: $" + format(self.__price, ".2f")
              + " | Stock: " + str(self.__stock))

    # ---- Conversion helpers (so the file code never touches private attributes) ----
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    