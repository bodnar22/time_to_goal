from json import loads as jloads
from datetime import datetime
from requests import get
import base64
import pprint


# api_token = "***********************************"  # API монобанку


def b64decode(text):  # функція для декодування
    result = base64.b64decode(text.encode("ascii"))
    return result.decode("ascii")


def timenow():  # функція для отримання поточного часу
    return datetime.today().strftime("%B %d %H:%M:%S")


def get_currency():  # отримуємо курси валют та записуємо в файл, токен не потрібен
    req = get("https://api.monobank.ua/bank/currency").text
    if "errorDescription" not in req:
        with open("currency.json", "w") as f:
            f.write(req)
        print(f'{timenow()}: Done')
    else:
        print(f'{timenow()}: Error')


def print_currency():  # виводимо цікаві для нас валюти в консоль
    with open("currency.json", "r") as f:
        cur = jloads(f.read())
    # res = str('Купівля/Продаж')
    res = f'\nUSD: {cur[0]["rateBuy"]}/{cur[0]["rateSell"]}'
    res = f'\n {cur[0]["rateSell"]}'
    # res += f'\nEUR: {cur[1]["rateBuy"]}/{cur[1]["rateSell"]}'
    return res


# def get_info():  # отримуємо баланс по рахунках, потрібен токен
#     api = get("https://api.monobank.ua/personal/client-info", headers={'X-Token': api_token}).json()
#     pprint.pprint(api)

target_amount = 1200 * print_currency()
uah_amount = 3200
usd_amount = 0
amount_usd_now = (uah_amount / float(print_currency())) + float(usd_amount)
monthly_put = 1900 / float(print_currency())
daily_put = monthly_put / 30
try:
    ttgl = float(target_amount) / float(daily_put)
except ValueError:
    pass

days_count = 1000
today_plus = None


def ttg():  # timetogoal
    today_plus = input("Введіть додану суму в грн: ")
    uah_amount += today_plus
    days_count = ttgl - (amount_usd_now / ttgl)
    return days_count


get_currency()
print(print_currency())
# get_info()
ttg()
