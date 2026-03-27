# This function asks for and validates the product name entered by the user
def Name():
    Name_product = input("Ingrese el nombre del producto: ").strip()
    if not Name_product:
        print ("No puede estar vacio este apartado, intente nuevamente.")
        return Name()
    else:
        return Name_product

# This function asks for the product price and validates any possible errors
def price():
    try:
        price_product = int(input("Ingrese el precio del producto: "))
        if price_product < 0:
            print ("No puedes ingresar numeros negativos, intente nuevamente.")
            return price()
        else:
            return price_product
    except ValueError:
        print ("No puedes ingresar letras, intente nuevamente.")    
        return price()    

# This function asks for the product quantity and validates any possible errors
def quantity():
    try:
        quantity_product = int(input("Ingrese la cantidad del producto: "))
        if quantity_product < 0:
            print ("No puedes ingresar numeros negativos, intente nuevamente.")
            return quantity()
        else:
            return quantity_product
    except ValueError:
        print ("No puedes ingresar letras, intente nuevamente.")    
        return quantity()

# Here the functions are called so they execute and their results are stored in their respective variables, and the corresponding calculations are performed
name_product = Name()
price_product = price()
quantity_product = quantity()
total = price_product * quantity_product

# This is where everything is printed
print("\nNombre del producto:",name_product,"\nPrecio del producto:",price_product,"\nCantidad del producto:",quantity_product,"\nTotal:",total)