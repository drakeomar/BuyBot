from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pickle
import json
import requests
import imaplib, email
import html2text
import base64
import subprocess
import os

with open('bb_config.json') as f:
    configData = json.load(f)
    
cvv = configData["cvv"]

check_urls = configData["check_urls"]

user = configData["email_user"]
password = configData["email_password"]
imap_url = configData["imap_url"]

login = configData["ne_login"]

item_number_str = ""

filename = 'CheckoutApi'
#button_xpath = '/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[9]/div[1]/div/div/div/button'
#item_url = 'https://www.bestbuy.com/site/lg-34wl500-b-34-ips-led-ultrawide-fhd-freesync-monitor-with-hdr-hdmi-black/6329954.p?skuId=6329954'
#setup chromeoptions
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#following options added to enable functionality with headless browser
#   and avoid elementclickintercepted error
options.add_argument('--window-size=1920,1080')
options.add_argument('--start-maximized')
#create webdriver instance for firefox

#autoChrome.get(item_url)
#autoChrome.find_element_by_xpath(button_xpath).click()

#autoChrome.get('https://bestbuy.com/cart')
#autoChrome.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()

#current_url = autoChrome.current_url
#wait for URL to change with 10 second timeout
#WebDriverWait(autoChrome, 10).until(EC.url_changes(current_url))

#login_field = autoChrome.find_element_by_xpath('//*[@id="fld-e"]')
#login_field.send_keys('drake@wirecutcompany.com')

#sign into newegg
def sign_in():
    return 0

#connect to email, parse most recent email from Newegg(containing ver code)
#   and extract and return ver code
def retrieve_ver_code():
    return 0


#parse response from within curl output file-- checkout_response
#   in order to obtain sessionId used for final checkout url
#   IMPORTANT: must not include response headers
def retrieve_Session_ID():
    with open(filename) as f:
        content = f.readlines()

    json_parser = json.loads(content[0])
    print("SESSION ID: ")
    print(content)
    print(json_parser["SessionID"])
    return(json_parser["SessionID"])


#dumps current cookies from webdriver
def dump_cookies():
    pickle.dump(autoChrome.get_cookies(), open("cookies.pk1","wb"))

#returns a list of dict objects that are each individual cooki
def load_cookies():
    return pickle.load(open("cookies.pk1","rb"))

#extract cookies from loaded pickled cookie data
#   parse list of dicts, pulling cookie name and value
#   to be converted into a format passable to a curl command
def extract_cookies(cookies_list):
    str = "'"
    for cookie in cookies_list:
        cookie_name = cookie["name"]
        cookie_value = cookie["value"]

        str+= cookie_name + "=" + cookie_value + "; "

    str = str[:-2]
    str += "'"
    #print("EXTRACT COOKIES:")
    #print(str)
    return str


def update_cookies(cookies_list):
    for cookie in cookies_list:
        cookie_name = cookie["name"]
        cookie_value = cookie["value"]
        cookie_domain = cookie["domain"]
        #print(cookie_name + ": " + cookie_value + ", " + cookie_domain)
        s.cookies.set(cookie_name, cookie_value, domain=cookie_domain)

#generate key to be used for checkout api request to obtain Session ID
def generate_key():
    str = build_str(item_number_str)
    return base64.b64encode(bytes(str, 'utf-8'))

#build payload for add2cart request
def build_str(string):
    return '{"SaleType":1,"ItemGroup":1,"ItemNumber":"'+ string + '","OptionalInfos":[]}'

def build_payload(item_num):
    payload_1 = " --data-binary '{\"ItemList\":[{\"ItemNumber\":\""
    payload_1 += item_num
    payload_2 = "\",\"ItemKey\":\""
    payload_2 += key
    payload_3 = """","Quantity":1,"ItemGroup":"Single"}],"Actions":[]}' 'https://secure.newegg.com/shop/api/CheckoutApi' -O """

    return payload_1 + payload_2 + payload_3

#use formatting to build custom string for curl command to Checkout API
def build_checkout_request(key, item_num):
    str = """curl -s -k -X 'POST' -H 'Host: secure.newegg.com' -H 'Connection: close' -H 'Content-Length: 202' -H 'sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="88"' -H 'Accept: application/json, text/plain, */*' -H 'X-Requested-With: XMLHttpRequest' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://secure.newegg.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Referer: https://secure.newegg.com/shop/cart' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9'"""

    dump_cookies()
    cookies_list = load_cookies()

    cookies = " -b " +  extract_cookies(cookies_list)

    #print("COOKIES FOR CHECKOUT_REQUEST")
    #print(cookies)

    payload = build_payload(item_num)
    #target = ' \'https://secure.newegg.com/shop/api/CheckoutApi\' -o \'testing.txt\' '
    cmd = str + cookies + payload

    print(cmd)
    return cmd

def build_checkout_url(session_id):
    base_url = 'https://secure.newegg.com/shop/checkout?sessionId='
    return(base_url + session_id)

#returns current time in milliseconds
def current_milli_time():
    return round(time.time() * 1000)

#checks the stock inventory of items in related json file
def check_stock():
    with open('itemNumbers.json') as f:
        data = json.load(f)

    while True:
        for item in data["gpus"]["3080"]:
            last = current_milli_time()
            page = requests.get(item["url"])
            soup = BeautifulSoup(page.content, 'html.parser')

            inventory = soup.find("div", {"class":"product-inventory"})
            checker = inventory.text
                    #print(inventory)
                    #print(inventory.text)

            if inventory.text.strip() == "OUT OF STOCK.":
                print(item["item_number"] + " ITEM IS STILL OUT OF STOCK ", end="", flush=True)
                print('Time Taken: ', end="", flush=True)
                print(current_milli_time() - last, end="", flush=True)
                print("ms")
            else:
                print("ITEM IS IN STOCK")
                break
        if checker.strip() != "OUT OF STOCK.":
            return item["item_number"]
            #else:
                #print("ERROR PARSING HTML OR UNEXPECTED CONDITION")



##PROGRAM STARTS##
#create chromedriver instance, headless, maximized for options
autoChrome = webdriver.Chrome('./chromedriver', chrome_options=options)

autoChrome.get('https://newegg.com')
autoChrome.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[4]/div[1]/div[1]/a').click()
login_field = autoChrome.find_element_by_xpath('//*[@id="labeled-input-signEmail"]')
#current_url = autoChrome.current_url
#wait for URL to change with 10 second timeout
#WebDriverWait(autoChrome, 1000).until(EC.url_changes(current_url))

login_field.send_keys(login)
print(autoChrome.title)
autoChrome.find_element_by_id('signInSubmit').click()
print("username input successful")

print("attempting to retrieve verification code...")

time.sleep(5)
connection = imaplib.IMAP4_SSL(imap_url)
connection.login(user, password)
connection.select('Inbox')


result, data = connection.uid('search', None, '(FROM "info@newegg.com")')
if result == 'OK':
    num = data[0].split()[-1]
    result, data = connection.uid('fetch', num, '(RFC822)')
    if result == 'OK':
        email_message = email.message_from_bytes(data[0][1])

        text = f"{email_message.get_payload(decode=True)}"
        html = text.replace("b'", "")
        h = html2text.html2text(html)


        output = h.replace("\\r\\n","")
        output = output.replace("'", "")
        result = output.find("verification code on our website:")


        #print(output)
        #print(result)
        result = result + 38
        end_result = result + 8
        verification_code = output[result:end_result].strip()

        print("Done")

connection.close()
connection.logout()


#time.sleep(5)
first_box = autoChrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[1]')
first_box.send_keys(verification_code[0])
second_box = autoChrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[2]')
second_box.send_keys(verification_code[1])
third_box = autoChrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[3]')
third_box.send_keys(verification_code[2])
fourth_box = autoChrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[4]')
fourth_box.send_keys(verification_code[3])
fifth_box = autoChrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[5]')
fifth_box.send_keys(verification_code[4])
sixth_box = autoChrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[6]')
sixth_box.send_keys(verification_code[5])

autoChrome.find_element_by_id('signInSubmit').click()
#time.sleep(20) #when manual entry is required
print("verification code submitted")
time.sleep(2)

item_number_str = check_stock()
#cookie extraction
dump_cookies()

#print(autoChrome.get_cookies())

#cookie loading for requests
cookies = load_cookies()
extract_cookies(cookies)

#print(cookies_list) #OLD
s = requests.Session()

#assign cookies to session
update_cookies(cookies)


#time.sleep(5)
#print(s.cookies)
#add item to cart
null = None
add2cart_response = s.post('https://www.newegg.com/api/Add2Cart',json={"ItemList":[{"ItemGroup":"Single","ItemNumber":item_number_str,"Quantity":1,"OptionalInfos":null,"SaleType":"Sales"}],"CustomerNumber":"WIhJrLSe0yzXwKdSJwU0JPBreL/EOp/A"})
print(add2cart_response.status_code )
print("Item successfully added to cart")
#print(add2cart_response.text)
#print(add2cart_response.text)
#print(s.cookies)
#print(add2cart_response.status_code)

print("generating key...")
key = generate_key()
key = str(key).replace("b'", "")
key = key[:-1]
print("key = " + key)

command = build_checkout_request(key, item_number_str)

#os.system(curl_cmdautoChrome.find_element_by_xpath('//*[@id="verificationCode"]'))
#os.system(command)
subprocess.call(command, shell=True)
time.sleep(1)

session_id = retrieve_Session_ID()

#get secure checkout page utilizing Session_ID in url
checkout_url = build_checkout_url(session_id)
autoChrome.get(checkout_url)

#time.sleep(10)

cvv_field = autoChrome.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/input')
cvv_field.click()
cvv_field.send_keys(cvv)
#autoChrome.execute_script("arguments[0].value = '732'", cvv_field)

#time.sleep(2)

############BUY ITEM###############
#autoChrome.find_element_by_xpath('//*[@id="btnCreditCard"]').click()
#print(checkout_response.text)
#print(checkout_response.status_code)

time.sleep(3)
autoChrome.close()
autoChrome.quit()
