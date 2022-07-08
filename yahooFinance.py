import yfinance as yf
print("Hello World!")
msft = yf.Ticker("MSFT")
goog = yf.Ticker('goog')
data = goog.history()
print(data.head())