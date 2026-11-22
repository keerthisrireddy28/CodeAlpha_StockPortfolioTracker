#STOCK PORTFOLIO TRACKER

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = []
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")

for stock_name, stock_price in stock_prices.items():
    print(stock_name, "- $", stock_price)

while True:
    try:
        number_of_stocks = int(input("\nHow many stocks do you want to enter? "
        ))

        if number_of_stocks > 0:
            break

        print("Please enter a positive number.")

    except ValueError:
        print("Please enter a valid whole number.")

for stock_number in range(number_of_stocks):

    print("\nStock", stock_number + 1)

    while True:
        stock_name = input(
            "Enter stock symbol: "
        ).strip().upper()

        if stock_name in stock_prices:
            break

        print("Stock not found. Try again.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                break

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")

    stock_price = stock_prices[stock_name]
    investment = stock_price * quantity

    stock_details = {
        "name": stock_name,
        "quantity": quantity,
        "price": stock_price,
        "investment": investment
    }

    portfolio.append(stock_details)
    total_investment += investment

print("\n================================")
print("        PORTFOLIO SUMMARY")
print("================================")

for stock in portfolio:
    print("Stock:", stock["name"])
    print("Quantity:", stock["quantity"])
    print("Price per share: $", stock["price"])
    print("Investment: $", stock["investment"])
    print("--------------------------------")

print("Total Portfolio Value: $", total_investment)

save_choice = input(
    "\nDo you want to save the portfolio? (yes/no): "
).strip().lower()

if save_choice == "yes":

    with open("portfolio.txt", "w", encoding="utf-8") as file:

        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=======================\n")

        for stock in portfolio:
            file.write("Stock: " + stock["name"] + "\n")
            file.write(
                "Quantity: " + str(stock["quantity"]) + "\n"
            )
            file.write(
                "Price per share: $" + str(stock["price"]) + "\n"
            )
            file.write(
                "Investment: $" + str(stock["investment"]) + "\n"
            )
            file.write("-----------------------\n")

        file.write(
            "Total Portfolio Value: $" + str(total_investment)
        )

    print("Portfolio saved to portfolio.txt!")

else:
    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")
