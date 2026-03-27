#Here the menu is stored with each option offered by the system, and the inventory is also located here
menu = ['Add product','Show inventory','Calculate statistics','Delete product','Exit']
inventory = []

#This function creates a new product and then adds it to the inventory, it also validates any type of error
def add_product():
    name = input('\nEnter the name of the product: ').upper()
    while True:
        try:
            price = int(input('Enter the price of the product: '))
            quantity = int(input('Enter the quantity of the product: '))
            if price <= 0 or quantity < 0:
                print ('Invalid option, try again.')
            else:
                producto = {'name':name,'price':price,'quantity':quantity}
                return producto
        except ValueError:
            print ('Invalid option, try again.')

#This function validates whether the option chosen by the user is correct and is in the menu
def opcion():
    while True:
        try:
            selected = int(input('Choose the option you want to perform: '))
            if selected < 1 or selected > 5:
                print ('Invalid option, try again.')
            else:
                return selected
        except ValueError:
            print ('Invalid option, try again.')
    

#This loop repeats the menu multiple times, executing each action the user wants to perform thanks to match; the program only ends if the user decides so
while True:
    print('\n------MENU------')
    for i,Emenu in enumerate(menu, start = 1):
        print(f'{i} - {Emenu}')
    selected_option = opcion()

    #match handles each option selected by the user
    match selected_option:
        case 1:
            # Add product to inventory
            new_product = add_product()
            inventory.append(new_product)
        case 2:
            #This if checks whether the inventory is empty, if not, it goes to the else and prints all the products
            print('\n-----INVENTORY-----')
            if not inventory:
                print ('The inventory is empty.')
            else:
                for i,products in enumerate(inventory):
                    print(f"{i + 1}. Product: {products['name']} - Price produtc {products['price']} - Quantity {products['quantity']} - total {products['price']*products['quantity']}")
            
        case 3:
            total = 0
            total_product = 0
            for i in inventory:
                #The for loop goes through each dictionary in the list, finds the price and quantity, multiplies them, and adds them to the total counter
                total += i['price'] * i['quantity']
                #Here it only finds the quantity and adds it to the total_product counter
                total_product += i['quantity']
            print('\n------------------------STATISTICS-------------------------')
            print('The total value of the inventory is', total)
            print(f'The total number of product types in the inventory is {len(inventory)}')
            print('The total number of products in the inventory is', total_product)
        case 4:
            if not inventory:
                print ('The inventory is empty.')
            else:
                #This if checks if there is nothing in the inventory, if there are products and it goes to the else, first asks for the product to delete, if it doesn’t exist it prints that the product doesn’t exist, but if it does exist, it deletes the product the user wants to remove
                delete = input('\nWhich product do you want to delete?: ').upper()
                for key in inventory:
                    if key['name'] == delete:
                        inventory.remove(key)
                        print('The product', delete, 'has been successfully deleted!')
                        break
                else:
                    print('That product is not found in the inventory')
        case 5:
            print ('You have exited the program successfully')
            break