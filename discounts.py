import datetime

class Discounts:
    def __init__(self):
        # Offers for specific items on specific days
        self.offers = {
            'Friday': {1: 0.10, 2: 0.15},  # 10% off on Pizza, 15% off on Burger on Fridays
            'Wednesday': {3: 0.20, 5: 0.50}  # 20% off on Pasta, 50% off on Juice on Wednesdays
        }

    def get_current_day(self):
        return datetime.datetime.now().strftime("%A")  # Get current day

    def apply_offers(self, order_items, menu):
        current_day = self.get_current_day()
        total_discount = 0.0

       
        for i, (item_name, quantity, price) in enumerate(order_items):
            # Find the item ID from the menu (by matching the item name)
            for id, item in menu.items.items():
                if item['name'] == item_name and current_day in self.offers and id in self.offers[current_day]:
                    discount = self.offers[current_day][id]
                    discount_amount = price * discount
                    total_discount += discount_amount
                    order_items[i] = (item_name, quantity, price - discount_amount)
                    print(f"Applied {int(discount * 100)}% discount on {item_name}: -Rs{discount_amount:.2f}")
        
        return total_discount
