import json
import time
import requests
import bestbuy
from bs4 import BeautifulSoup

headers = {'Host':'www.bestbuy.com',  'Accept':'application/json', 'Content-Type':'application/json; charset=UTF-8', 'Origin':'https://www.bestbuy.com', 'User-Agent':'";Not A Brand";v="99", "Chromium";v="88"', 'Accept-Encoding':'identity', 'Accept-Language':'en-US,en;q=0.9' }

proxy = {'http': 'http://user-sp412c491a:wirecut2021@us.smartproxy.com:10000',
         'https': 'http://user-sp412c491a:wirecut2021@us.smartproxy.com:10000'}

test_url_1 = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
check_urls = [ "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149", "https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163" ]
#use proxy
#page = requests.get(test_url_1, headers=headers, proxies=proxy)

def get_current_milli_time():
    return round(time.time() * 1000)

while True:
    #no proxy: testing
    last = get_current_milli_time()

    page = requests.get(check_urls[0], headers=headers, proxies=proxy)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    inventory = soup.find("button", {"class": "add-to-cart-button"})

    if inventory == None:
        print("ERROR LOADING/PARSING HTML: RESETTING FOR NEW ATTEMPT")
        continue

    #print(inventory)
    #print(inventory.text)


    #print(inventory)
    print('Time Taken: ', end="", flush=True)
    print(get_current_milli_time() - last, end="", flush=True)
    print(" ms : ", end="", flush=True)
    print(inventory.text)

    if inventory.text.strip() != "Sold Out":
        break

print("SUCCESS - ITEM IN STOCK, COMMENCING BUY")
