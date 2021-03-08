
#SETUP
import requests
import json
import os
import csv
from datetime import datetime
from dotenv import load_dotenv
import seaborn
import pandas
import matplotlib.pyplot as plt

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

##CURRENT DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y at %H:%M")

##USER INPUT FOR TICKER
symbol = input("Please enter the stock symbol you're researching:")

if symbol.isalpha() and len(symbol) <= 5:
    ticker = symbol.upper()
else:
    print("Please make sure you entered your stock symbol correctly! For example, 'MSFT' for Miscrosoft.")
    exit()

#REQUESTING DATA
load_dotenv()

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"

response = requests.get(request_url)  

parsed_response = json.loads(response.text)

#####Need to add backup in case of failure (e.g. ticker passes initial validation but doesn't actually represent a real stock)


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

##RECOMMENDATION
if float(latest_close) <= (1.2 * float(recent_low)):
    rec = "BUY!"
    rec_reason = "This stock may be undervalued as its price is less than 20 percent above its recent low."
else:
    rec = "HOLD OFF!"
    rec_reason = "This stock may be risky - its current price is greater than 20 percent above its recent low and it could be volatile."


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

csv = pandas.read_csv(csv_file_path)
res = seaborn.lineplot(x="timestamp", y="close", data=csv)

#csv["timestamp"] = pandas.to_datetime(csv["timestamp"], format = "%y-%m-%d")
#The chart will work without this, but the dates will be illegible. Figure out how to format.
plt.title(f"Historical Pricing Data for {ticker}")
plt.xlabel("Date")
plt.ylabel("Closing Price")
res.yaxis.set_major_formatter('${x:1.2f}')
plt.show()

##Add formatting here



##UI
print("-------------------------")
print(f"SELECTED SYMBOL: {ticker}")
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
print(f"CREATING CSV at {csv_file_path}")
print("-------------------------")
print("GRAPHING RECENT PRICE HISTORY...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")