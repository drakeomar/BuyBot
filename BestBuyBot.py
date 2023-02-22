import requests
import time
import datetime
import json
from BestBuyBotHelper import Bestbot

class item_node:
    def __init__(self, url=None, desc=None):
        self.url = url
        self.desc = desc
        self.next = None

with open('bb_config.json') as f:
    configData = json.load(f)
    
filename_test =  'bestbuyapitest.txt'

proxy = {'http': configData["proxy1"],
         'https': configData["proxy2"]}

base_url = "https://api.bestbuy.com/v1/products(sku="

end_url = configData["end_url"]

url_start_idx = 40
url_end_idx = 47

aList = []
bList = []


def get_current_milli_time():
    return round(time.time() * 1000)

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

def altElement(a):
    return a[::2]

def url_builder(url_file):
    skus_json = load_json(url_file)

    #headNode = skus_json["products"][0]

    for product in skus_json["products"]:
        #print(product["sku"])

        new_url = base_url + product["sku"] + end_url
        #bList.append(item_node(new_url, product["description"]))
        aList.append({'url':new_url, 'description':product["description"]})

        #aList.append(product["description"])

    print(aList)


#def get_orderability(url):
    #page_text = s.get(url)
    #if page_text.status_code == '200':
        #return json.loads(page_text.text)
    #else:
        #return None

url_builder('skus.json')

s = requests.Session()
header = {'user-agent':'curl/7.58.0', 'Accept-Encoding':'identity', 'Host':'api.bestbuy.com'}
s.headers.update(header)

counter = 0

sku_grab = ""


while not sku_grab:
    for item in aList:
        last = get_current_milli_time()
        page = s.get(item["url"])
        if page.status_code != 200:
            print("skipping")
            continue
        page_data = json.loads(page.text)

        #print(page_data)
        print(page_data['products'][0]['orderable'])

        #print(page.text)
        print("That request and parsing took.... ", end="", flush=True)
        print(get_current_milli_time() - last, end="", flush=True)
        print(" ms. Request #", end ="", flush=True)
        counter+=1
        print(counter, end="", flush=True)
        print(" for: ", end="", flush=True)
        print(item["description"], end="", flush=True)
        print(" . Current Time: ", end="", flush=True)
        print((str(datetime.datetime.now())))

        if page_data['products'][0]['orderable'] != "SoldOut":
            checker = False
            sku_grab = item["url"][url_start_idx:url_end_idx]
            break

        time.sleep(2)

print("ITEM IS IN STOCK, ORDERING NOW...")
a = Bestbot()
a.sign_in()
a.add_to_cart(sku_grab)
a.checkout(True)
del a
