
#SETUP
import requests
import json
import os
import csv
from datetime import datetime
from dotenv import load_dotenv

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

##CURRENT DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y at %H:%M")

##USER INPUT FOR TICKER


#Need to do data validation here (make sure symbol is 1-5 letters [not numbers or special characters])
###if incorrect, display friendly error message like "Please check make sure your stock symbol is correct, for example, "MSFT" for Microsoft."


#REQUESTING DATA
load_dotenv()

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

ticker = "IBM" #> will need to prompt user input here

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"

response = requests.get(request_url)  

parsed_response = json.loads(response.text)

#####Need to add backup in case of failure (e.g. ticker passes initial validation)


##INFORMATION
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) #assumes first day is on top, may want to sort to be sure

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))
recent_high = max(high_prices)
recent_low = min(low_prices)

##Dictionary keys are "Meta Data" and "Time Series (Daily)"
#####Keys within "Meta Data" are dict_keys(['1. Information', '2. Symbol', '3. Last Refreshed', '4. Interval', '5. Output Size', '6. Time Zone'])
#####Keys within "Time Series (Daily)" are {'1. open', '2. high', '3. low', '4. close', '5. volume'}

##RECOMMENDATION
if float(latest_close) <= (1.2 * float(recent_low)):
    rec = "Buy!"
    rec_reason = "This stock may be undervalued."
else:
    rec = "Avoid!"
    rec_reason = "This stock may be too risky."


##CSV FILE:
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_price = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_price["1. open"],
            "high": daily_price["2. high"],
            "low": daily_price["3. low"],
            "close": daily_price["4. close"],
            "volume": daily_price["5. volume"]
        })

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
print(f"RECOMMENDATION: {rec}")
print(f"RECOMMENDATION REASON: {rec_reason}")
print("-------------------------")
print(f"CREATING CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")