import yfinance as yf

aapl = yf.Ticker("AAPL")

print(aapl.quarterly_balancesheet)