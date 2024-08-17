import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(symbol):
    stock_ticker = yf.Ticker(symbol)
    historical_data = stock_ticker.history(period="5y")
    return historical_data

def analyze_data(data):
    data["30-day MA"] = data["Close"].rolling(window=30).mean()
    return data

def visualize_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data["Close"], label="Closing Price")
    plt.plot(data.index, data["30-day MA"], label="30-day Moving Average", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("NIFTY 50 Stock Price Analysis")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    symbol = "^NSEI"  # Use the correct symbol for the NIFTY 50 index
    data = fetch_stock_data(symbol)
    if data.empty:
        print("No data found for the symbol. Please check the symbol and try again.")
    else:
        analyzed_data = analyze_data(data)
        visualize_data(analyzed_data)

if __name__ == "__main__":
    main()
