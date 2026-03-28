from menu import menu
from validations import validate_int
from services import add_product, show_products, search_product, delete_product, update_product, statistics
from archivo import save_csv, upload_csv
inventory = []

while True:
    print('\n--------------MENU--------------')
    for i,menu_ in enumerate(menu, start=1):
        print(f'{i} - {menu_}')
    option = validate_int('Choose an option: ', min_value=1, max_value=9)

    match option:
        case 1:
            inventory.append(add_product())
        case 2:
            show_products(inventory)
        case 3:
            search_product(inventory)
        case 4:
            update_product(inventory)
        case 5:
            delete_product(inventory)
        case 6:
            statistics(inventory)
        case 7:
            save_csv(inventory)
        case 8:
            upload_csv(inventory)
        case 9:
            print('Program finished successfully!')
            break
