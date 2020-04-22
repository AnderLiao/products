# Create a product list and the price for each product.
# User can manually input the name and price of product.

# Create the product list for new input
products =[]
while True:
	product = input('Product: ') # Create the product
	if product == 'q':
		break
	price = int(input('Price: ')) # Create the price of product
	products.append([product, price])
print(products)

# Show the product list
for product in products:
	print(product)

# Create the CSV file and save the data accordingly
with open('product_list.csv', 'w', encoding='utf-8') as file:
	file.write('品項,價格\n')
	for product in products:
		file.write(product[0] + ',' + str(product[1]) + '\n')