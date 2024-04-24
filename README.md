# Online Shopping Cart

This project implements an online shopping cart system using Python. It consists of two main classes: ItemToPurchase and ShoppingCart. 
The program allows users to add, remove, modify items in the cart, as well as output the items' descriptions and the total cost of the cart.

## ItemToPurchase Class
1. Attributes:
  -  item_name: string
  -  item_price: int
  -  item_quantity: int
  -  item_description: string

2. Default constructor initializes attributes with default values.

3. Methods:
  - print_item_cost(): Prints the item's cost based on quantity and price.
  - print_item_description(): Prints the item's description.

## ShoppingCart Class
1. Attributes:
  - customer_name: string
  - current_date: string
  - cart_items: list of ItemToPurchase objects

2. Default constructor initializes attributes with default values.

3. Methods:
  - add_item(item): Adds an item to the cart.
  - remove_item(item_name): Removes an item from the cart.
  - modify_item(modified_item): Modifies an item's quantity in the cart.
  - get_num_items_in_cart(): Returns the total quantity of items in the cart.
  - get_cost_of_cart(): Returns the total cost of items in the cart.
  - print_total(): Prints the total cost of the items in the cart.
  - print_descriptions(): Prints descriptions of all items in the cart.

## Main Section
1. Prompts the user for a customer's name and today's date, and creates a ShoppingCart object.

2. Provides a menu for the user to interact with the shopping cart:
  - 'a': Add item to cart
  - 'r': Remove item from cart
  - 'c': Change item quantity
  - 'i': Output items' descriptions
  - 'o': Output shopping cart
  - 'q': Quit

3. Executes the chosen option by calling the appropriate method of the ShoppingCart object.
