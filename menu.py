# Order System
order = []

# Menu Items
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49}
}

# Display Menu and Take Order
while True:
    print("\nMenu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['Item name']} - ${value['Price']}")
    
    menu_selection = input("Enter the number of your selection: ")
    
    if not menu_selection.isdigit():
        print("Error: Please enter a valid number.")
        continue
    
    menu_selection = int(menu_selection)
    
    if menu_selection not in menu_items:
        print("Error: Selection not in menu items.")
        continue
    
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]
    
    quantity_input = input(f"Enter the quantity for {item_name} (default is 1): ")
    if not quantity_input.isdigit():
        quantity = 1
    else:
        quantity = int(quantity_input)
    
    order.append({"Item name": item_name, "Price": price, "Quantity": quantity})
    
    while True:
        keep_ordering = input("Do you want to keep ordering? (y/n): ").strip().lower()
        match keep_ordering:
            case 'y':
                break
            case 'n':
                print("Thank you for your order.")
                break
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue
        if keep_ordering == 'n':
            break
    if keep_ordering == 'n':
        break

# Print Receipt
print("\nYour Order Receipt:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    
    item_name_space = " " * (26 - len(item_name))
    price_space = " " * (6 - len(f"{price:.2f}"))
    quantity_space = " " * (8 - len(str(quantity)))
    
    print(f"{item_name}{item_name_space}| ${price:.2f}{price_space}| {quantity}{quantity_space}")

total_price = sum(item["Price"] * item["Quantity"] for item in order)
print("--------------------------|--------|----------")
print(f"Total Price: ${total_price:.2f}")
