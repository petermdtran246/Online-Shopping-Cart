class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        self.new_item_price = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price}'
              f' = ${self.new_item_price}')

    def print_item_description(self):
        self.item_quantity = 12 * self.item_quantity
        print(f'{self.item_name}: {self.item_description}, {self.item_quantity} oz.')




