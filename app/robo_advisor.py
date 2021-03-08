
#SETUP
import requests
import json
from datetime import datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

##USER INPUT FOR TICKER



##CURRENT DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y at %H:%M")

##MAKING REQUEST/INFO GRAB
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)  
#print(type(response)) #>requests.model.response
#print(response.status_code) #>200
#print(response.text) 

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close = parsed_response["Time Series (Daily)"][f"{last_refreshed}"]["4. close"]

recent_high = parsed_response["Time Series (Daily)"][f"{last_refreshed}"]["2. high"]

recent_low = parsed_response["Time Series (Daily)"][f"{last_refreshed}"]["3. low"]

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