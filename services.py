from validations import validate_int, validate_float
from menu import options

def add_product():
    name = input('\nEnter the name of the product: ').upper()
    price = validate_float('Enter the price of the product: ', min_value=0.01)
    quantity = validate_int('Enter the quantity of the product: ', min_value=0) 
    print('Product added successfully!')
    return{
        'name': name,
        'price': price,
        'quantity': quantity
    }
    
def show_products(inventory):
#This if checks whether the inventory is empty, if not, it goes to the else and prints all the products
    print('\n-----INVENTORY-----')
    if not inventory:
        print ('The inventory is empty.\n')
    else:
        for i,products in enumerate(inventory):
            print(f"{i + 1}. Product: {products['name']} - Price: {products['price']} - Quantity: {products['quantity']} - Total: {products['price']*products['quantity']}")

def search_product(inventory):
    if not inventory:
                print ('The inventory is empty.\n')
    else:
        search = input('\nWhich product do you want to search for?: ').upper()
        for product in inventory:
            if product['name'] == search:
                print(f"Product found: {product['name']} - Price: {product['price']} - Quantity: {product['quantity']}")
                break
        else:
            print('That product is not found in the inventory')

def update_product(inventory):
    if not inventory:
                print ('The inventory is empty.\n')
    else:
        search = input('\nWhich product do you want to update?: ').upper()
        for product in inventory:
            if product['name'] == search:
                for option in options:
                    print(option)
                choice = validate_int('Enter your choice (1-4): ', min_value=1, max_value=4)

                match choice:
                    case 1:                        
                        new_name = input('Enter the new name of the product: ').upper()
                        product['name'] = new_name
                    case 2:
                        new_price = validate_float('Enter the new price of the product: ', min_value=0.01)
                        product['price'] = new_price   
                    case 3:
                        new_quantity = validate_int('Enter the new quantity of the product: ', min_value=0)
                        product['quantity'] = new_quantity  
                    case 4:
                        new_name = input('Enter the new name of the product: ').upper()
                        new_price = validate_float('Enter the new price of the product: ', min_value=0.01)
                        new_quantity = validate_int('Enter the new quantity of the product: ', min_value=0)
                        product['name'] = new_name
                        product['price'] = new_price  
                        product['quantity'] = new_quantity  
                print('Product updated successfully!')
                break
        else:
            print('That product is not found in the inventory')

def delete_product(inventory):
    if not inventory:
                print ('The inventory is empty.')
    else:
        #This if checks if there is nothing in the inventory, if there are products and it goes to the else, first asks for the product to delete, if it doesn’t exist it prints that the product doesn’t exist, but if it does exist, it deletes the product the user wants to remove
        delete = input('\nWhich product do you want to delete?: ').upper()
        for product in inventory:
            if product['name'] == delete:
                inventory.remove(product)
                print('The product', delete, 'has been successfully deleted!')
                break
        else:
            print('That product is not found in the inventory')

def statistics(inventory):
    if not inventory:
        print('The inventory is empty.')
        return
    total = 0
    total_product = 0
    most_expensive_product = {"price": 0}
    product_greater_quantity = {"quantity": 0}

    for i in inventory:
        total += i['price'] * i['quantity']
        total_product += i['quantity']
        
    for product in inventory:
        if product['price'] > most_expensive_product['price']:
            most_expensive_product = product
        if product['quantity'] > product_greater_quantity['quantity']:
            product_greater_quantity = product


    print('\n------------------------STATISTICS-------------------------')
    print('The total value of the inventory is', total)
    print(f'The total number of product types in the inventory is {len(inventory)}')
    print('The total number of products in the inventory is', total_product)
    print('The most expensive product is', most_expensive_product['name'], 'with a price of', most_expensive_product['price'])
    print('The product with greater quantity is', product_greater_quantity['name'], 'with a quantity of', product_greater_quantity['quantity'])