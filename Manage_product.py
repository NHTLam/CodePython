products = {} # 1 product includes id and name

def add_product():
    id = int(input('Enter product id: '))
    name = input('Enter product name: ')
    if id in products:
        print(f'Sorry, product {id} is already have')
    else:
        products[id] = name
        print(f'Product {id} is {name}')
    
def edit_product():
    id = int(input('Enter product id: '))
    if id in products:
        name = input('Enter product name: ')
        products[id] = name
        print(f'Update successful, product {id} is {name}')
    else:
        print(f'Sorry, Product {id} is a new product')

def del_product():
    id = int(input('Enter product id: '))
    if id in products:
        del products[id]
        print('Delete, Successfully')
    else:
        print(f'Sorry, Product {id} is a new product')

while True:
    print('1. Add product')
    print('2. Show product')
    print('3. Delete product')
    print('4. Edit product')
    print('5. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        add_product()
    elif choice == '2':
        print(products)
    elif choice == '3':
        del_product()
    elif choice == '4':
        edit_product()
    elif choice == '5':
        break
    else:
        print('Invalid choice')

