import csv
from datetime import datetime

# Hardcoded stock prices (dictionary)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 415,
    "RELIANCE": 2900,
    "TCS": 3800,
    "INFY": 1450,
}

def show_available_stocks():
    print("\n📈 AVAILABLE STOCKS:")
    print("-" * 30)
    print(f"{'Stock':<10} {'Price (₹/$)'}")
    print("-" * 30)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10} {price}")
    print("-" * 30)

def get_portfolio():
    portfolio = {}

    print("\n💼 STOCK PORTFOLIO TRACKER")
    print("=" * 40)
    show_available_stocks()

    print("\nApne stocks daalo (exit type karo band karne ke liye)")

    while True:
        stock_name = input("\nStock ka naam daalo: ").upper().strip()

        if stock_name == "EXIT":
            break

        if stock_name not in STOCK_PRICES:
            print(f"⚠️  '{stock_name}' available nahi hai! Upar list dekho.")
            continue

        try:
            quantity = int(input(f"{stock_name} ki quantity daalo: "))
            if quantity <= 0:
                print("⚠️  Quantity positive honi chahiye!")
                continue
        except ValueError:
            print("⚠️  Sirf number daalo!")
            continue

        # Portfolio mein add karo
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

        print(f"✅ {stock_name} x {quantity} add ho gaya!")

    return portfolio

def calculate_portfolio(portfolio):
    if not portfolio:
        print("\n⚠️  Portfolio khali hai!")
        return

    print("\n" + "=" * 50)
    print("📊 AAPKA PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<10} {'Qty':<8} {'Price':<12} {'Total Value'}")
    print("-" * 50)

    grand_total = 0

    results = []
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        total = price * qty
        grand_total += total
        print(f"{stock:<10} {qty:<8} {price:<12} ₹{total:,}")
        results.append([stock, qty, price, total])

    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':<30} ₹{grand_total:,}")
    print("=" * 50)

    # File mein save karo?
    save = input("\nResult CSV file mein save karna chahte ho? (haan/nahi): ").lower()
    if save == "haan" or save == "h":
        save_to_csv(results, grand_total)

def save_to_csv(results, grand_total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        writer.writerows(results)
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", grand_total])

    print(f"✅ Portfolio save ho gaya: {filename}")

if __name__ == "__main__":
    portfolio = get_portfolio()
    calculate_portfolio(portfolio)
    print("\n👋 Dhanyavaad! Invest karte rehna!")
