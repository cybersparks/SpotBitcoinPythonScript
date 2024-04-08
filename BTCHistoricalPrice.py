#This script will allow me to enter a date and get the spot BTC price for that day. 
#Documentaiton https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-prices

from itertools import count
import requests #Can handle HTTP requests / Can query data from websites
import json #JSON file parser library

#Ask user to input historical date for BTC Price
historical_date = input("Enter a date in the past in Year-MM-DD format to get the Spot BTC price for that date.")

#variable storing coinbase API URL in python Format
#Modified variable to get historical price
url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot?date={}'.format(historical_date)

#requests.get function, send the http request using url variable
response = requests.get(url)

#Process with the JSON loads function
spot_price = json.loads(response.text)
#show spot btc price
print(spot_price) 