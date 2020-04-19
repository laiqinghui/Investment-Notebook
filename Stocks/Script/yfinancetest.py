import yfinance as yf

sats = yf.Ticker("S58.SI")

fin = sats.financials
# get stock info
print(sats.financials)

