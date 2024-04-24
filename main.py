from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

# Prompt the user for a customer's name and today's date.
customer_name = input("Enter customer's name:\n")
today_date = input("Enter today's date:\n")
print("\nCustomer name:", customer_name)
print("Today's date:", today_date)

# Create an object of type ShoppingCart
cart = ShoppingCart()
cart.customer_name = customer_name
cart.current_date = today_date

# Call print_menu() method
def print_menu():
    # Prompt the user's choice of menu options
    print('\nMENU')
    print('a - Add item to cart')
    print('r - Remove item to cart')
    print('c - Change item quantity')
    print('i - Output items\'s description')
    print('o - Output shopping cart')
    print('q - Quit')


# Call execute_menu() method that takes 2 parameters
def execute_menu(choice, cart):
    if choice == 'o':
        output_shopping_cart(cart)
    elif choice == 'i':
        output_item_description(cart)
    elif choice == 'a':
        add_item_to_cart(cart)
    elif choice == 'r':
        remove_item_from_cart(cart)
    elif choice == 'c':
        change_item_quantity(cart)
    elif choice == 'q':
        print('Goodbye!')
        exit()
    else:
        print('Please try again.')


# Call output_shopping_cart() method
def output_shopping_cart(cart):
    cart.print_total()

# Call output_item_descriptions() method:
def output_item_description(cart):
    cart.print_descriptions()

# Call add_item_to_cart() method:
def add_item_to_cart(cart):
    item_name = input('Enter the item name:\n')
    item_description = input('Enter the item description:\n')
    item_price = int(input('Enter the item price:\n'))
    item_quantity = int(input('Enter the item quantity:\n'))

    item = ItemToPurchase()
    item.item_name = item_name
    item.item_description = item_description
    item.item_price = item_price
    item.item_quantity = item_quantity

    cart.add_item(item)
    print('Item added to cart.')

# Call remove_item_from_cart() method
def remove_item_from_cart(cart):
    item_name = input('Enter name of item to remove:\n')
    cart.remove_item(item_name)

# Call change_item_quantity() method
def change_item_quantity(cart):
    item_name = input('Enter the item name:\n')
    new_quantity = int(input('Enter the new quantity:\n'))

    item = ItemToPurchase()
    item.item_name = item_name
    item.item_quantity = new_quantity

    cart.modify_item(item)
    print('Item quantity changed.')

# Main loop
while True:
    print_menu()
    choice = input('Enter your choice: ').lower()
    execute_menu(choice, cart)






















