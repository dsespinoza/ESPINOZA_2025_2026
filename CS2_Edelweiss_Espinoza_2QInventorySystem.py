#Uses arrays to store product data
product_names = []
product_prices = []
product_quantities = []

# --- Error Handling Functions ---

def product_index(item):
    #Searches for a product and returns its index or -1 if not found.
    try:
        index = next(
            i for i, name in enumerate(product_names)
            if name.strip().lower() == item.strip().lower()
        )
        return index
    except StopIteration:
        return -1

def price_input(prompt):
    #This function helps to get and validate a positive float price.
    while True:
        try:
            price = input(prompt)
            value = float(price)
            #Price must be greater than 0
            if value <= 0:
                print("Price/Value cannot be less than or equal to 0!")
            else:
                return value
        except ValueError:
            print("Invalid format. Please enter a number.")

def quantity_input(prompt):
    #This function helps to get a non-negative integer quantity.
    while True:
        try:
            quantity = input(prompt)
            value = int(quantity)
            if value < 0:
                print("Quantity cannot be negative!")
            else:
                return value
        except ValueError:
            print("Invalid format. Please enter a whole number.")


# --- Main Functions ---

def display():
    #Displays the main menu options to the user.
    print("\n--- Inventory System Menu ---")
    print("[1] Add product (and initial quantity)")
    print("[2] Display/Sort all products")
    print("[3] Update a price")
    print("[4] Search for a product")
    print("[5] Delete a product")
    print("[6] Calculate Total Inventory Value")
    print("[7] Exit")
    print("----------------------------")

def add_product():
    #Prompts the user for product details.
    print("\n--- Add Product ---")
    
    #Get product name
    while True:
        name = input("Enter product name: ").strip()
        if name:
            if product_index(name) == -1: #Prevents duplicate names
                break
            print("Product already exists. Use the Update feature or choose a different name.")
        else:
            print("Product name cannot be empty. Please try again.")

    #Get product price 
    price = price_input("Enter product price: ")
    
    #Get initial quantity 
    quantity = quantity_input("Enter initial quantity in stock: ")

    #Add the product to the lists
    product_names.append(name)
    product_prices.append(price)
    product_quantities.append(quantity)
    print(f"'{name}' added: Price ${price:.2f}, Quantity {quantity}.")

def display_products():
    #This displays all products and allows for sorting.
    #Declares global variables because they will be reassigned if sorting occurs.
    global product_names, product_prices, product_quantities 
    
    print("\n--- Current Inventory ---")
    if not product_names:
        print("Inventory is empty. Add items first!")
        return

    while True:
        print("Sort by: [N]ame | [P]rice | [Q]uantity | [S]kip and Display (Default Order)")
        sort_choice = input("Enter choice: ").upper()

        if sort_choice == 'S':
            break

        #Combines lists into tuples for sorting
        inventory = list(zip(product_names, product_prices, product_quantities))

        if sort_choice == 'N':
            #Sort by Name (index 0)
            inventory.sort(key=lambda x: x[0].lower())
            print("--- Sorted by Name (A-Z) ---")
            break
        elif sort_choice == 'P':
            #Sort by Price (index 1)
            inventory.sort(key=lambda x: x[1])
            print("--- Sorted by Price (Lowest to Highest) ---")
            break
        elif sort_choice == 'Q':
            #Sort by Quantity (index 2)
            inventory.sort(key=lambda x: x[2], reverse=True)
            print("--- Sorted by Quantity (Highest to Lowest) ---")
            break
        else:
            print("Invalid sort choice. Please try again.")
            
    #Once sorting happens, update global lists with the new sorted order.
    if sort_choice != 'S':
        #Unpacks the sorted list back into the global arrays
        product_names, product_prices, product_quantities = zip(*inventory)
        
        #Convert tuples back to lists
        product_names = list(product_names)
        product_prices = list(product_prices)
        product_quantities = list(product_quantities)
        
    #Display the final list
    for i in range(len(product_names)):
        name = product_names[i]
        price = product_prices[i]
        qty = product_quantities[i]
        print(f"{i + 1}. {name} | Price: ${price:.2f} | Quantity: {qty}")

def update_price():
    #Allows user to search for a product by name and update its price.
    print("\n--- Update Price ---")
    if not product_names:
        print("Inventory is empty. Add items first!")
        return

    itemname = input("Enter item name to update price: ").strip()
    index_update = product_index(itemname)

    if index_update == -1:
        print("Item not found!")
        return

    #Get the new price 
    new_price = price_input(f"Enter new price for {product_names[index_update]}: ")

    #Update the price
    product_prices[index_update] = new_price
    print(f"Price for {product_names[index_update]} updated to ${new_price:.2f}.")

def search_product():
    #Allows user to search for a product by name and display its details.
    print("\n--- Search Product ---")
    if not product_names:
        print("Inventory is empty. Add items first!")
        return

    item_name = input("Enter item: ").strip()
    index_found = product_index(item_name)

    if index_found != -1:
        name = product_names[index_found]
        price = product_prices[index_found]
        qty = product_quantities[index_found]
        
        print("\n--- Product Details ---")
        print(f"Name: {name}")
        print(f"Price: ${price:.2f}")
        print(f"Quantity in Stock: {qty}")
    else:
        print("Product not found!")

def delete_product():
    #Allows user to search for a product by name and delete it.
    print("\n--- Delete Product ---")
    if not product_names:
        print("Inventory is empty. Nothing to delete.")
        return

    item_name = input("Enter item name to delete: ").strip()
    index_delete = product_index(item_name)

    if index_delete == -1:
        print("Item not found!")
        return

    deleted_name = product_names[index_delete]

    #Removes the item from all three arrays using the found index
    product_names.pop(index_delete)
    product_prices.pop(index_delete)
    product_quantities.pop(index_delete)
    
    print(f"'{deleted_name}' has been successfully removed from the inventory.")

def calculate_total_value():
    #Calculates and displays the total value of all inventory stock.
    print("\n--- Total Inventory Value ---")
    if not product_names:
        print("Inventory is empty. Total value is $0.00.")
        return
        
    total_value = 0.0
    #Calculates Total Value = Sum of (Price * Quantity)
    for price, quantity in zip(product_prices, product_quantities):
        total_value += price * quantity
        
    print(f"Total value of all items in stock: ${total_value:,.2f}")


def main():
    #The main control loop for the inventory system.
    while True:
        display()

        try:
            choice = input("Enter choice: ")
            choice = int(choice)

            if choice == 1:
                add_product()
            elif choice == 2:
                display_products()
            elif choice == 3:
                update_price()
            elif choice == 4:
                search_product()
            elif choice == 5:
                delete_product()
            elif choice == 6:
                calculate_total_value()
            elif choice == 7:
                print("Exiting Inventory System. Goodbye! 👋")
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu choice.")
main()






