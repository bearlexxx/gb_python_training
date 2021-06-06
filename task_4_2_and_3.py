import requests
from datetime import datetime

def currency_rates(currency):
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency not in response:
        return None

    cur_rate = response[response.find('<Value>', response.find(currency)) + 7:response.find('</Value>', response.find(currency))]
    cur_rate = float(cur_rate.replace(',', '.'))
    date_info = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, date_info)
    return f'Курс: {cur_rate}, на дату: {datetime(day=day, month=month, year=year)}'

currency = input('Введите код валюты (например, USD): ')
print(currency_rates(currency))
