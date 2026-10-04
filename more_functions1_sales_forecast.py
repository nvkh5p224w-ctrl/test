# More Functions 1 - Sales Forecast

def next_month_forecast(month, sales):
    month = month.strip().title()

    if month in ("Jan", "Feb", "Mar"):
        forecast_percent = 0.10
    elif month in ("Apr", "May", "Jun"):
        forecast_percent = 0.15
    elif month in ("Jul", "Aug", "Sep"):
        forecast_percent = 0.20
    elif month in ("Oct", "Nov", "Dec"):
        forecast_percent = 0.25
    else:
        raise ValueError("Invalid month.")

    return sales * (1 + forecast_percent)

def main():
    while True:
        do_program = input("Do you want to enter a sales forecast? (Yes/No): ").strip().lower()

        if do_program == "no":
            break
        if do_program != "yes":
            print("Please enter Yes or No.\n")
            continue

        last_name = input("Enter last name: ")
        month = input("Enter month (Jan-Dec): ")
        sales = float(input("Enter sales: "))

        forecast = next_month_forecast(month, sales)
        print(f"{last_name} next month's forecast: ${forecast:,.2f}\n")

if __name__ == "__main__":
    main()
