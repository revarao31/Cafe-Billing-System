from menu import Menu

class Order:
    def __init__(self):
        self.menu = Menu()
        self.order_items = []
        self.total = 0.0

    def take_order(self):
        while True:
            self.menu.display_menu()
            item_id = int(input("\nEnter the item number you want to order ( 0 to finish ): "))
            if item_id == 0:
                break
            if item_id in self.menu.items:
                quantity = int(input(f"How many {self.menu.items[item_id]['name']} do you want to order? "))
                item_price = self.menu.items[item_id]['price']
                self.order_items.append((self.menu.items[item_id]['name'], quantity, item_price * quantity))
                self.total += item_price * quantity
                print(f"{quantity} {self.menu.items[item_id]['name']} added to your order.\n")
            else:
                print("Invalid item number. Try again.")

    def get_total(self):
        return self.total

    def get_order_items(self):
        return self.order_items
