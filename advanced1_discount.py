# Advanced Functions 1 - Discount Amount and Discounted Price

def calculate_discount(quantity, price, discount_rate):
    original_total = quantity * price
    discount_amount = original_total * discount_rate
    discounted_price = original_total - discount_amount
    return discount_amount, discounted_price

def main():
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    discount_rate = float(input("Enter discount rate as a decimal (example: .10): "))

    discount_amount, discounted_price = calculate_discount(
        quantity, price, discount_rate
    )

    print(f"Quantity: {quantity:g}")
    print(f"Price: ${price:,.2f}")
    print(f"Discount Amount: ${discount_amount:,.2f}")
    print(f"Discounted Price: ${discounted_price:,.2f}")

if __name__ == "__main__":
    main()
