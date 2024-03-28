# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Hello! Welcome to the store!\n")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu category would you like to order? ")

    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    # refactored to use enumerate instead of the counter variable "i"
    for i, key in enumerate(menu.keys(), 1):
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        

    # Get the customer's input
    menu_category = input("Please enter your selected menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        # It's safe to assume menu_item.keys() are only integers, since
        # we used the indexes from enumerate() to set the menu_items dict keys
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}\n")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?\n")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i+=1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i+=1
            # 2. Ask customer to input menu item number
            menu_selection = input(
                "Please enter the item number of your selection:  ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    item_quantity = input(
                        f"How many {item_name}s would you like to order?  ")

                    # Check if the quantity is a number
                    if item_quantity.isdigit():
                        item_quantity = int(item_quantity)
                    else:
                        # default to 1 if item_quantity is not a number
                        item_quantity = 1

                    # Add the item name, price, and quantity to the order list
                    ordered_item = {
                        "Item name": item_name,
                        "Price": menu_items[menu_selection]["Price"],
                        "Quantity": item_quantity
                    }
                    order_list.append(ordered_item)
                    # Tell the customer that their input isn't valid

                else:
                    # Tell the customer they didn't select a menu option
                    print(f"Sorry, {menu_selection} is not a valid menu option.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu category option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
            case 'y':
                # Keep ordering
                place_order = True
                break
            case 'n':
                # Exit the keep ordering question loop
                place_order = False
                # Since the customer decided to stop ordering, thank them for
                # their order
                print('Thank you for your order')
                # Exit the keep ordering question loop
                break
            case _:
                # Tell the customer to try again
                print("Please enter 'Y' or 'N'")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
# print('menu check: \n') # remove after testing
# print(order_list) # remove after testing

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
if order_list:
    for item in order_list:
        # 7. Store the dictionary items as variables
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # 8. Calculate the number of spaces for formatted printing

        # Instead of manually counting hyphens, let's take the given formatting
        # to calculate the total width of each column
        item_column_width = len('--------------------------')
        price_column_width = len('--------')
        quantity_column_width = len('----------')

        # Subtract the string length of the item name, price, quantity from
        # their respective total column widths to get the total spaces needed
        num_item_spaces = item_column_width - len(item_name)
        # let's subtract an extra 2 for a leading white space an a $ sign
        num_price_spaces = (price_column_width - len(str(price))) - 2
        num_quantity_spaces = quantity_column_width - len(str(quantity))

        # 9. Create space strings
        item_spaces_string = " " * num_item_spaces
        price_spaces_string = " " * num_price_spaces
        quantity_spaces_string = " " * num_quantity_spaces

        # 10. Print the item name, price, and quantity
        print(f"{item_name}{item_spaces_string}| ${price}{price_spaces_string}"
              f"| {quantity}{quantity_spaces_string}")
else:
    print("You didn't order anything.")


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum([item["Price"] * item["Quantity"] for item in order_list])
print(f"Your order total is ${total_cost:,.2f}")
