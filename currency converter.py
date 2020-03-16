# Currency Converter

import requests, json

api_key = "ox4932x4j9wokz7c28k1rfln0blujv8e8v3h1lnxgm2syrrcxz4y6s4k7z33"

base_url = "http://metals-api.com/api/"

url = "http://metals-api.com/api/latest?access_key="+api_key

response = requests.get(url)

x = response.json()

'''response which we get in json format
for i in x:
    print(i)    
for _ in x['rates']:
    print(_,end='\t')  '''

base_currency = str(input('\nWhat will be your base currency ?\nChoose from above currency code'))

desired_currency_exchange = str(input('Desired Currency : '))

complete_url = "http://metals-api.com/api/convert?access_key="+api_key+"&from="+base_currency+"&to="+desired_currency_exchange+"&amount=1"

response  = requests.get(complete_url)

x = response.json()

print('hence 1'+base_currency+' = '+str(round(x['result'],2))+desired_currency_exchange)
