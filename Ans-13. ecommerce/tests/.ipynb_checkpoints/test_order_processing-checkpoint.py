import unittest
from ecommerce.order_processing.order import Order
from ecommerce.order_processing.payment import Payment
from ecommerce.product_management.product import Product

class TestOrderProcessing(unittest.TestCase):
    def test_order(self):
        product = Product("Laptop", 1200, "SKU123")
        order = Order(1, product, 2)
        self.assertEqual(order.get_order_summary(), "Order ID: 1, Product: Laptop, Quantity: 2")

    def test_payment(self):
        product = Product("Laptop", 1200, "SKU123")
        order = Order(1, product, 2)
        payment = Payment(order, 2400, "Credit Card")
        self.assertEqual(payment.process_payment(), "Processing payment of 2400 for Order ID: 1 using Credit Card")

if __name__ == "__main__":
    unittest.main()
