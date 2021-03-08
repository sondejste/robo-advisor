
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

#breakpoint()

##Dictionary keys are "Meta Data" and "Time Series (Daily)"
#####Keys within "Meta Data" are dict_keys(['1. Information', '2. Symbol', '3. Last Refreshed', '4. Interval', '5. Output Size', '6. Time Zone'])

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
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
    ##will need to use IF statements here
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")