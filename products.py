import os

def read_file(filename):
    # Create an empty list
    products = []
    # Read the file
    with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if '品項,價格' in line:
                    continue # In case the header will be rewritten again
                product, price = line.strip().split(',')
                products.append([product, price])
    return products

def user_input(products):
    # Add the product and price
    while True:
        # User can manually input the name and price of product.
        product = input('Product: ') # Create the product
        if product == 'q':
            break
        price = int(input('Price: ')) # Create the price of product
        products.append([product, price])
    return(products)

def print_products(products):
    # Show the new and updated product list
    for product in products:
        print(product)

def write_file(filename, products):
    # Create or update the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('品項,價格\n')
        for product in products:
            file.write(product[0] + ',' + str(product[1]) + '\n')
            # No need to return the value when writing data to csv file instead of reading
        print('Complete..')

def main():
    # Check the file
    filename = 'product_list.csv'
    if os.path.isfile(filename):
        print('Reading..')
        products = read_file(filename)
    else:
        print('File not found..')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)
main()