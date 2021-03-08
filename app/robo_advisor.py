
#SETUP
import requests
import json
from datetime import datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

##USER INPUT FOR TICKER


##Need to do data validation here (make sure symbol is 1-5 letters [not numbers or special characters])
####if incorrect, display friendly error message like "Please check make sure your stock symbol is correct, for example, "MSFT" for Microsoft."

#GET Request to Alphavantage API to retrieve data (user has already input API key into .env file)
#MAKE HTTP Request for trading data

##CURRENT DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y at %H:%M")

##MAKING REQUEST/INFO GRAB
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)  

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) #assumes first day is on top, may want to sort to be sure

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]


high_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
recent_high = max(high_prices)

low_prices = []

for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))
recent_low = min(low_prices)

#breakpoint()

##Dictionary keys are "Meta Data" and "Time Series (Daily)"
#####Keys within "Meta Data" are dict_keys(['1. Information', '2. Symbol', '3. Last Refreshed', '4. Interval', '5. Output Size', '6. Time Zone'])
#####Keys within "Time Series (Daily)" are {'1. open', '2. high', '3. low', '4. close', '5. volume'}

##RECOMMENDATION



##UI
print("-------------------------")
print("SELECTED SYMBOL: IBM")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {dt_string}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
    ##will need to use IF statements here
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#NEED TO ALSO WRITE FOLLOWING INFO ONTO A CSV FILE AS WELL:
#