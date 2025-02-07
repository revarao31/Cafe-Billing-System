def show_menu():
    menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Salad": 4.99,
        "Pasta": 7.99,
        "Soda": 1.99
    }
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    return menu

def show_discounts(menu):
    discounts = {
        "Burger": 0.10,  # 10% discount
        "Pizza": 0.15,   # 15% discount
        "Salad": 0.05,   # 5% discount
        "Pasta": 0.20,   # 20% discount
        "Soda": 0.00     # No discount
    }
    print("\nDiscounts:")
    for item, discount in discounts.items():
        discounted_price = menu[item] * (1 - discount)
        print(f"{item}: ${discounted_price:.2f} (Discount: {discount * 100:.0f}%)")

if __name__ == "__main__":
    menu = show_menu()
    show_discounts(menu)