class Bill:
    def __init__(self, order_items, total):
        self.order_items = order_items
        self.total = total

    def generate_bill(self):
        print("\n--- Bill ---")
        for item, quantity, price in self.order_items:
            print(f"{quantity} x {item} - Rs{price:.2f}")
        print(f"\nTotal: Rs{self.total:.2f}")
