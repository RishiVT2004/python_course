import json
from requests import get
from pprint import PrettyPrinter #helps to get nicely formated outputs for json... 
import currencyapicom

api_key = "cur_live_kJH7ttaF7rWv9gpV8GOL9bokDpim5s59VW4VBwUZ";
base_url = "https://api.currencyapi.com/"

printer = PrettyPrinter()

def get_currency():
    endpoint = f"v3/latest?apikey={api_key}"    
    url = base_url + endpoint
    data = get(url).json()['data']

    data = list(data.items())
    data.sort()

    return data



#key data to be resolved -: gets 'code' , 'value' wrt to usd

def print_currencies(currencies):
    print(f"values wrt 1 $ ")
    print('-----------------')
    for _id,currency in currencies: # always return data in get_currency()
        _id = currency['code']
        value = currency['value']
        print(f"{_id} - {value} ") 


def exchange_rate(curr1,curr2): #curr1,curr2 -> currency id
    endpoint = f"v3/convert?q={curr1}_{curr2}&compact=ultra&apikey={api_key}"
    url = base_url+endpoint
    response = get(url)

    data = response.json()
    printer.pprint(data)


data_curr = get_currency()
print_currencies(data_curr)

exchange_rate("USD","INR")

