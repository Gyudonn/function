import os

outside_products = []

operation = input('Please input the write or read mode: ')


def if_file_isexit():
	if os.path.isfile('product.csv'):
		print('File is exist.')
	else:
		print('File is not exitt')

def file_edit_mode(operation):
	if operation == 'w':
		write_file('product.csv', outside_products)
	elif operation == 'r' :
		read_file('product.csv', outside_products)	

def write_file(filename, products):
	while True:
		name = input('input the product name: ')
		if name == 'q':
			with open(filename, operation, encoding = 'utf-8') as f:
				f.write('Good,Price\n')
				for product in products:
					f.write(product[0] + ',' + str(product[1]) + '\n')
			break
		price = input('input the product price: ')
		products.append([name, price])
	return products

def read_file(filename, products):	
	with open('product.csv' , operation, encoding = 'utf-8') as file:
		for line in file:
			if 'Good,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

def print_product(products):
	print(products)
	for product in products:
		print('The price of ' + product[0] + ' is ' + str(product[1]))

if_file_isexit()
file_edit_mode(operation)
print_product(outside_products)

