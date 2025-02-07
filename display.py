# main.py
from order import Order
from bill import Bill
from discounts import Discounts

def display():
    print("Welcome to the RR's Cafe!")
    
    # Step 1: Take the Order
    order = Order()
    order.take_order()

    # Step 2: Check if any items were ordered
    if order.get_order_items():
        # Step 3: Apply Discounts
        discounts = Discounts()
        discount_amount = discounts.apply_offers(order.get_order_items(), order.menu)

        # Step 4: Generate the Bill
        total_with_discounts = order.get_total() - discount_amount
        bill = Bill(order.get_order_items(), total_with_discounts)
        bill.generate_bill()
    else:
        print("No items ordered.")

if __name__ == "__main__":
    display()
