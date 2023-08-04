products = {'computer': [1000, 20],
            'printer': [500, 10],
            'monitor': [200, 15],
            'mouse': [50,100]}
    
def edit_product():
    name = input('Enter product name: ')
    if name in products:
        new_price = int(input('Enter product price: '))
        products[name][0] = check_price(new_price)
        print(f'Update successful, This product is priced at ${check_price(new_price)}')
    else:
        print(f'Sorry, Something went wrong!')

def buy_product():
    name = input('Enter product name: ')
    n = int(input('Enter number of products you want to buy: '))
    if name in products:
        products[name][1] -= check_product_quantity(n, products[name][1])
        print('Buy Successfully')
    else:
        print(f'Sorry, Product {name} is wrong')

def check_price(price):
    if price > 0:
        return price
    else:
        print('Product can not < 0')
        price = int(input('Enter product price: '))
        return check_price(price)

def check_product_quantity(n, old_quantity):
    if n < old_quantity:
        return n
    else:
        print('The number of products you want to buy is too much')
        n = int(input('Enter number of products you want to buy: '))
        return check_product_quantity(n, old_quantity)           

while True:
    print('1. Show product')
    print('2. Buy product')
    print('3. Edit price')
    print('4. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        print(products)
        print(products.items())
        print(products.keys())
        print(products.values())
        print(products.pop('computer'))
    elif choice == '2':
        buy_product()
    elif choice == '3':
        edit_product()
    elif choice == '4':
        break
    else:
        print('Invalid choice')
    