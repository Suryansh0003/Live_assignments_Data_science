class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def get_order_summary(self):
        return f"Order ID: {self.order_id}, Product: {self.product.name}, Quantity: {self.quantity}"
