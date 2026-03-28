import csv
ruta = './data/inventory.csv'
def save_csv(inventory):
    with open(ruta, 'w', newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'price', 'quantity'])
        writer.writeheader()
        writer.writerows(inventory)
        print('Saved successfully!')

def upload_csv(inventory):
    with open(ruta, 'r', newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            price = float(row['price'])
            quantity = int(row['quantity'])
            product = {"name":name,"price":price,"quantity":quantity}
            inventory.append(product)
            print('Loaded successfully!')

