# Check the file
products = []
with open('product_list.csv', 'r', encoding='utf-8') as file:
	for line in file:
		if '品項,價格' in line:
			continue # In case the header will be rewritten again
		product, price = line.strip().split(',')
		products.append([product, price])
print(products)


# Add the product and price
while True:
	# User can manually input the name and price of product.
	product = input('Product: ') # Create the product
	if product == 'q':
		break
	price = int(input('Price: ')) # Create the price of product
	products.append([product, price])
print(products)

# Show the new/updated product list
for product in products:
	print(product)

# Create or update the file
with open('product_list.csv', 'w', encoding='utf-8') as file:
	file.write('品項,價格\n')
	for product in products:
		file.write(product[0] + ',' + str(product[1]) + '\n')