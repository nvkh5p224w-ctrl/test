# More Functions 2 - Automobile Out-the-Door Price

def out_the_door_price(msrp, make, model, electric_code):
    make_model = f"{make.strip().lower()} {model.strip().lower()}"

    if make_model == "honda accord":
        discount_percent = 0.10
    elif make_model == "toyota rav4":
        discount_percent = 0.15
    elif electric_code.strip().upper() == "Y":
        discount_percent = 0.30
    else:
        discount_percent = 0.05

    discounted_price = msrp * (1 - discount_percent)
    total = discounted_price * 1.07
    return total

def main():
    total_msrp = 0.0
    total_sales_price = 0.0

    while True:
        do_program = input("Do you want to enter an automobile? (Yes/No): ").strip().lower()

        if do_program == "no":
            break
        if do_program != "yes":
            print("Please enter Yes or No.\n")
            continue

        make = input("Enter make: ")
        model = input("Enter model: ")
        electric_code = input("Electric vehicle? (Y/N): ")
        msrp = float(input("Enter MSRP: "))

        sales_price = out_the_door_price(msrp, make, model, electric_code)

        print(f"{make} {model} out-the-door price: ${sales_price:,.2f}\n")

        total_msrp += msrp
        total_sales_price += sales_price

    print(f"Total MSRP: ${total_msrp:,.2f}")
    print(f"Total Sales Price: ${total_sales_price:,.2f}")

if __name__ == "__main__":
    main()
