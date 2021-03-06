import re

import bs4
import requests


def fetching_price(link):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 '
                      'Safari/537.36',
    }
    res = requests.get(link, headers=HEADERS)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    item_price = soup.select('#priceblock_ourprice')
    final_price = int(
        "".join(re.findall(r'>(.+?)<', str(item_price[0]))).replace('₹', '').strip().replace(',', '').split('.')[0])
    return final_price


def price_comparision(market_price, budget_price):
    if market_price < budget_price:
        print(
            "Current Price of item on Amazon is {} and Your budget is {}, Buy it!!".format(market_price, budget_price))
    else:
        print("Current Price of item on Amazon is {} and Your budget is {}, Wait!!".format(market_price, budget_price))


if __name__ == '__main__':
    website_link = input("Please provide the amazon website link : ")
    budget = int(input("Please provide your budget amount : "))
    price = fetching_price(website_link)
    if price:
        price_comparision(price, budget)
