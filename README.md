# python
def generate_bill():
    print("Welcome to the Bill Generator!")
    print("="*30)
    items = []
    total = 0
    tax_rate = 0.05  # 5% tax
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
            price = float(input(f"Enter price per unit for {item_name}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
            continue
        item_total = quantity * price
        items.append((item_name, quantity, price, item_total))
        total += item_total
    # Calculate tax and final amount
    tax = total * tax_rate
    final_amount = total + tax
    # Print the bill
    print("\n========== BILL ==========")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Total"))
    print("-"*45)
    for item in items:
        print("{:<15} {:<10} {:<10.2f} {:<10.2f}".format(item[0], item[1], item[2], item[3]))
    print("-"*45)
    print(f"Subtotal: {total:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Final Total: {final_amount:.2f}")
    print("=========================")
    print("Thank you for shopping!")
generate_bill()

