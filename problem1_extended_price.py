# Problem 1 - Extended Price
# Enter 0 for quantity to stop.

def compute_extended_price(quantity, unit_price):
    total = quantity * unit_price
    if total > 10000:
        total *= 0.90
    return total

def main():
    total_ext_price = 0.0

    while True:
        quantity = float(input("Enter quantity (0 to stop): "))
        if quantity == 0:
            break

        unit_price = float(input("Enter unit price: "))
        extended_price = compute_extended_price(quantity, unit_price)

        print(f"Quantity: {quantity:g}")
        print(f"Price: ${unit_price:,.2f}")
        print(f"Extended Price: ${extended_price:,.2f}\n")

        total_ext_price += extended_price

    print(f"Total Extended Price: ${total_ext_price:,.2f}")

if __name__ == "__main__":
    main()
