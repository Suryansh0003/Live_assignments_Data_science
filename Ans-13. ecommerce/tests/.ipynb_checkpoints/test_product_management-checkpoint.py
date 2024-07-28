import unittest
from ecommerce.product_management.product import Product
from ecommerce.product_management.inventory import Inventory

class TestProductManagement(unittest.TestCase):
    def test_product(self):
        product = Product("Laptop", 1200, "SKU123")
        self.assertEqual(product.get_details(), "Product: Laptop, Price: 1200, SKU: SKU123")

    def test_inventory(self):
        inventory = Inventory()
        product = Product("Laptop", 1200, "SKU123")
        inventory.add_product(product)
        self.assertEqual(inventory.list_products(), ["Product: Laptop, Price: 1200, SKU: SKU123"])

if __name__ == "__main__":
    unittest.main()
