# Create a product list and the price for each product.
# User can manually input the name and price of product.

products =[]
while True:
	product = input('Product: ') # Create the product
	if product == 'q':
		break
	price = input('Price: ') # Create the price of product
	products.append([product, price])
print(products)
print(products[1]) # Get first product
print(products[0][1]) # Get the price of first product