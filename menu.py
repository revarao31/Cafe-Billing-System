class Menu:
    def __init__(self):
        self.items = {
            1: {'name': 'Pizza', 'price': 800},
            2: {'name': 'Burger', 'price': 200},
            3: {'name': 'Pasta', 'price': 300},
            4: {'name': 'Fries', 'price': 450},
            5: {'name': 'Juice', 'price': 500}
        }

    def display_menu(self):
        print("\n--- Menu ---")
        for id, item in self.items.items():
            print(f"{id}. {item['name']} - Rs{item['price']}")