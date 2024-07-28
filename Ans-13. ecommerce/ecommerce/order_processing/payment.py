class Payment:
    def __init__(self, order, amount, payment_method):
        self.order = order
        self.amount = amount
        self.payment_method = payment_method

    def process_payment(self):
        return f"Processing payment of {self.amount} for Order ID: {self.order.order_id} using {self.payment_method}"
