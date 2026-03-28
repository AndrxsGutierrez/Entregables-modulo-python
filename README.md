📦 Inventory System

This is a simple inventory management system developed in Python. It allows you to add, display, search, update, delete products, and view inventory statistics.
Data is stored in a CSV file.

---

✨ Features

* Add products to the inventory
* Show all products
* Search products by name
* Update products (name, price, quantity)
* Delete products
* View statistics:

  * Total products
  * Most expensive product
  * Product with the highest quantity
* Save and load inventory from a CSV file

---

⚙️ Requirements

* Python 3.x
* No external libraries required

---

🚀 Installation

1. Clone or download the project to your machine
2. Make sure Python is installed

---

▶️ Usage

1. Run the main file:

```
python app.py
```

2. Follow the interactive menu to manage the inventory

---

## 📌 Menu Options

1. Add products
2. Show products
3. Search products
4. Update products
5. Delete products
6. View statistics
7. Save inventory to file
8. Load inventory from file
9. Exit

---

## 🗂️ Project Structure

* app.py → Main file (controls menu and program flow)
* services.py → Business logic (CRUD operations)
* validations.py → User input validations
* menu.py → Menu definitions
* archivo.py → CSV file handling
* data/inventory.csv → Inventory database

---

🧪 Example Usage

* Run the program
* Select option **1** to add a product
* Enter name, price, and quantity
* Use option **2** to view the inventory

---

⚠️ Troubleshooting

* If there are errors loading the CSV:

  * Make sure `data/inventory.csv` exists
  * Verify it has the correct headers: `name, price, quantity`

* If the program does not start:

  * Ensure all files are in the same folder
  * Enter valid numeric values for price and quantity

---

📌 Notes

* This project is designed for learning purposes
* The code is simple and easy to understand
* You can modify and expand it as need

📄 License

This project is free to use.
You can modify and adapt it as you wish.
