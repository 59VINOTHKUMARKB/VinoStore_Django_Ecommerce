from base.models import Product_table
products_data = [
    {'product_name': 'Red T shirt', 'stock': 10, 'price': 50.00},
    {'product_name': 'Black Jeans', 'stock': 5, 'price': 75.00},
    {'product_name': 'Blue T shirt', 'stock':10, 'price': 50.00},
    {'product_name': 'Black Shoes', 'stock': 3, 'price': 75.00},
    {'product_name': 'White Sneakers', 'stock': 5, 'price': 75.00},
    {'product_name': 'Black Watch', 'stock': 5, 'price': 175.00},
]

for data in products_data:
    product = Product_table(**data)
    product.save()
