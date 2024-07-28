class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku

    def get_details(self):
        return f"Product: {self.name}, Price: {self.price}, SKU: {self.sku}"
