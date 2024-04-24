from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    # Call default constructor with 3 attributes
    def __init__(self):
        self.customer_name = 'none'
        self.current_date = 'January 1, 2016'
        self.cart_items = []

    # Call the 1st add_item() methods
    def add_item(self, item):
        self.cart_items.append(item)

    # Call the 2nd remove_item() methods
    def remove_item(self, item_name):
        # Loop through cart items
        for item in self.cart_items:
            # Check if item name match:
            if item.item_name == item_name:
                # Remove item from cart_items list
                self.cart_items.remove(item)
                return
        print('item not found in cart. Nothing removed.')

    # Call the 3rd modify_item() method
    def modify_item(self, modified_item):
        # Loop through cart items
        for item in self.cart_items:
            # Check if item name match
            if item.item_name == modified_item:
                # Modify quantity
                item.item_quantity = modified_item.item_quantity
        print('Item not found in cart. Nothing modified')

    # Call the 4th get_num_items_in_cart() method
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    # Call the 5th get_cost_of_cart() method
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
        return total_cost

    # Call the 6th print_total() method
    def print_total(self):
        # Check if cart is empty
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
            return
        print(f"{self.customer_name}'s shopping Cart - {self.current_date}")
        # Print the number of items in the cart
        print('Number of items: ', self.get_num_items_in_cart())
        # Print an empty line
        print()
        # Loop through each item in the cart
        for item in self.cart_items:
            item.print_item_cost()
        print()
        print(f"Total: ${self.get_cost_of_cart()}")

    # Call the 7th print_descriptions() method
    def print_descriptions(self):
        # Check if cart is empty
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print('Items Descriptions')
        # Loop through each item in the cart
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)

















