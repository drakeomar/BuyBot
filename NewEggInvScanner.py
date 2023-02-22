import json
import time
import requests
from bs4 import BeautifulSoup

with open('bb_config.json') as f:
    configData = json.load(f)
    
check_urls = configData["check_urls"]

checker = "OUT OF STOCK."

#proxies = { 'http':'http://35.185.16.35:80','https':'https://35.185.16.35:80'}
proxy = { 'https': config_data["proxy_1"]}
def current_milli_time():
    return round(time.time() * 1000)

#last = current_milli_time()

with open('itemNumbers.json') as f:
    data = json.load(f)

def check():

    while True:
        for item in data["gpus"]["3080"]:
            last = current_milli_time()
            page = requests.get(item["url"], proxies=proxy)
            #print(page.text)
            soup = BeautifulSoup(page.content, 'html.parser')

            inventory = soup.find("div", {"class":"product-inventory"})
            #checker = inventory.text
                #print(inventory)
                #print(inventory.text)

            if inventory.text.strip() == "OUT OF STOCK.":
                print(item["item_number"] + " ITEM IS STILL OUT OF STOCK ", end="", flush=True)
                print('Time Taken: ', end="", flush=True)
                print(current_milli_time() - last, end="", flush=True)
                print("ms")
            elif inventory.text.strip() == "In stock.":
                print("ITEM IS IN STOCK")
                break
            else:
                print("ERROR PARSING HTML OR UNEXPECTED CONDITION")

check()
