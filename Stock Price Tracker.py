import yfinance as yf
import time
from datetime import datetime

def track_stock(symbol, refresh_interval=10):
    print(f"Tracking stock: {symbol.upper()} (updates every {refresh_interval} seconds)")
    print("-" * 60)

    while True:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d", interval="1m")

        if data.empty:
            print("No data found. Please check the symbol.")
            break

        latest = data.iloc[-1]
        current_price = latest['Close']
        open_price = data.iloc[0]['Open']
        change = current_price - open_price
        percent_change = (change / open_price) * 100

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{now} | Price: ${current_price:.2f} | Change: {change:+.2f} ({percent_change:+.2f}%)")
        time.sleep(refresh_interval)

# Example usage
if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol (e.g., AAPL, MSFT, TSLA): ").upper()
    interval = input("Refresh interval in seconds (default 10): ")
    interval = int(interval) if interval.strip().isdigit() else 10
    track_stock(stock_symbol, interval)

