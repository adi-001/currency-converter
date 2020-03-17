# Currency Converter
# To get your own api key, sign up for free @https://metals-api.com/
import requests, json

api_key = "---Copy your api here---"

# Asks for user to input base currency
base_currency = str(input('\nWhat will be your base currency ?\nChoose from above currency code'))

# Asks for user to input desired currency 
desired_currency_exchange = str(input('Desired Currency : '))

complete_url = "http://metals-api.com/api/convert?access_key="+api_key+"&from="+base_currency+"&to="+desired_currency_exchange+"&amount=1"

# GET requests method to retrieve data from specified url
response  = requests.get(complete_url)

# Getting the retrieved data in json format
x = response.json()

# To check what response did you get,  you can comment out this region and run below code
'''
for i in x:
    print(i) 
 ## Displays all countries currency code   
for _ in x['rates']:
    print(_,end='\t')   '''


print('hence 1'+base_currency+' = '+str(round(x['result'],2))+desired_currency_exchange)
