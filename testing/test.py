from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pickle
import json
import requests
import imaplib, email
import html2text
import base64
import subprocess
import os

user = 'drake@wirecutcompany.com'
password = 'JanuarySTG@041288'
imap_url = 'imap.gmail.com'
cvv = "732"

login = 'drake@wirecutcompany.com'

item_number_str = '9SIA6RA5R38891'

filename = 'testing.txt'
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

cmd = """curl -i -s -k -X 'POST' -H 'Host: secure.newegg.com' -H 'Connection: close' -H 'Content-Length: 202' -H 'sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="88"' -H 'Accept: application/json, text/plain, */*' -H 'X-Requested-With: XMLHttpRequest' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://secure.newegg.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Referer: https://secure.newegg.com/shop/cart' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -b 'NVTC=248326808.0001.ef2j6lxh1.1615427345.1615427345.1615427345.1; NSC_mc-tfdvsf.ofxfhh.dpn-ttm=5ccba3d87a48996e4086c61eb85a30bda2fb8a3b9cf7de9c611100f3a7aeda0779fef01f; NV%5FW57=USA; NV%5FW62=en; _ga=GA1.2.475563883.1615427350; _gid=GA1.2.1114059615.1615427350; mt.v=2.674966914.1615427350270; mt.sc=%7B%22i%22%3A1615427350508%2C%22d%22%3A%5B%5D%7D; usprivacy=1YNY; OptanonAlertBoxClosed=2021-03-11T01:49:13.908Z; _cc=AbvbKHtSyj02MqvvuHlKREdk; s_ecid=MCMID%7C03255817928126783589076863573363058613; NID=1j1j722Q9D346I1j721cef954f0e7e1413b52bf91eff4d03c5b; AMCVS_1E15776A524450BC0A490D44%40AdobeOrg=1; s_cc=true; NV%5FSPT=; NV%5FCARTOTHERINFO=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22ct1%22%3a%220%22%7d%2c%22Exp%22%3a%221615513785%22%7d%7d%7d; NV%5FCUSTOMERLOGIN=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22sj%22%3a%220%22%2c%22sb%22%3a%22NdTZGLsi966F0Uw94FVBpgigavOcGLusp2w6cnDEUsqKw30kUgLJ792Rae0Ka13DTIP7VwdJAnw%253d%22%2c%22sd%22%3a%22drake%2540wirecutcompany.com%22%2c%22sc%22%3a%2280750583%22%2c%22si%22%3a%22Drake%2bOmar%22%7d%2c%22Exp%22%3a%222562112185%22%7d%7d%7d; NV%5FOTHERINFO=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22sb%22%3a%22NdTZGLsi966F0Uw94FVBpgigavOcGLusp2w6cnDEUsqKw30kUgLJ792Rae0Ka13DTIP7VwdJAnw%253d%22%2c%22sd%22%3a%22NdTZGLsi966F0Uw94FVBpgigavOcGLusp2w6cnDEUsqKw30kUgLJ792Rae0Ka13DTIP7VwdJAnw%253d%22%2c%22sc%22%3a%22WIhJrLSe0yzXwKdSJwU0JPBreL%252fEOp%252fA%22%2c%22si%22%3a%22Drake%2bOmar%22%2c%22se%22%3a%22PxM3OuUxGpfJs2ZXEcchwocjgLujpLmu%22%2c%22s115%22%3a%220nNMDJV3VOjhhOc68MAw6Q%253d%253d%22%2c%22sn%22%3a%225996517224877620210310174945%22%7d%2c%22Exp%22%3a%222562112185%22%7d%7d%7d; NV%5FDVINFO=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22w19%22%3a%22Y%22%2c%22s81%22%3a%2280750583%22%7d%2c%22Exp%22%3a%221615513750%22%7d%7d%7d; NV%5FTOKEN=VM47j51UVJzWSByasaTLtdM3fMFKMq3gydm8KAPWe%2bpRtmc1IjRltzBDL%2beJh%2fXBJMIi6QxPhlVXkHGXshX3amIIOMMCaCXKtpMaAAi65zDXYBwrF4Vr9MbKLbeoJfeepPJiKyV4eyvETxRY0Kc0xTw7Oy1qsb2PFIGWDXJOta44lq3CJxdcDYSC2YKZHN9s%2brJewUDtU1Ac%2bBbYJQ%2fDCA%3d%3d; NV%5FS115=0nNMDJV3VOjhhOc68MAw6Q%3d%3d; NV%5FCONFIGURATION=#5%7B%22Sites%22%3A%7B%22USA%22%3A%7B%22Values%22%3A%7B%22w58%22%3A%22USD%22%2C%22w61%22%3A%221646963348267%22%2C%22w57%22%3A%22USA%22%7D%2C%22Exp%22%3A86400000000%7D%7D%7D; NV%5FPREVIOUSSERVERNAME=#5%7B%22Sites%22%3A%7B%22USA%22%3A%7B%22Values%22%3A%7B%22sr%22%3A%22E11%22%7D%2C%22Exp%22%3A0%7D%7D%7D; NV%5FLASTTICK=F40hmwKcT-Js7PMehjTbrA; OptanonConsent=isIABGlobal=false&datestamp=Wed+Mar+10+2021+17%3A49%3A54+GMT-0800+(Pacific+Standard+Time)&version=6.6.0&hosts=&consentId=d791ff17-757c-4544-a115-013542680713&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CBG2%3A1&AwaitingReconsent=false&geolocation=US%3BCA; utag_main=v_id:01781ef92e9f001758422da7103603073001706b00bd0$_sn:1$_se:4$_ss:0$_st:1615429194344$ses_id:1615427350180%3Bexp-session$_pn:4%3Bexp-session; mt.visits=%7B%22lastVisit%22%3A1615427394716%2C%22visits%22%3A%5B1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%5D%7D; s_sess=%20s_cpc%3D0%3B; _uetsid=13f454f0820c11eba11edfda3aee2339; _uetvid=13f50f30820c11eb92e255fc6dafc84a; mp_newegg_mixpanel=%7B%22distinct_id%22%3A%20%221781ef942750-0a6c0b90e654ee-53e3566-1fa400-1781ef942761db%22%2C%22bc_persist_updated%22%3A%201615427355747%2C%22customer_country%22%3A%20%22US%22%2C%22bc_id%22%3A%20-1719187002%7D; NV_NVTCTIMESTAMP=1615427396; _fbp=fb.1.1615427395495.869584855; AMCV_1E15776A524450BC0A490D44%40AdobeOrg=870038026%7CMCIDTS%7C18698%7CvVersion%7C5.0.0%7CMCMID%7C03255817928126783589076863573363058613%7CMCAID%7CNONE%7CMCOPTOUT-1615434594s%7CNONE%7CMCAAMLH-1616032194%7C9%7CMCAAMB-1616032194%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18705; _gcl_au=1.1.1284837441.1615427396; stc118799=tsa:1615427395984.2140253103.4459858.9557153693393563.:20210311021955|env:1%7C20210411014955%7C20210311021955%7C1%7C1083032:20220311014955|uid:1615427395983.1674479533.3924637.118799.1383876643:20220311014955|srchist:1083032%3A1%3A20210411014955:20220311014955; xyz_cr_100393_et_137==&cr=100393&wegc=&et=137&ap=; s_pers=%20s_vs%3D1%7C1615429250639%3B%20gpv_pv%3Dshopping%2520cart%7C1615429250656%3B%20s_nr%3D1615427450667-New%7C1646963450667%3B%20gpvch%3Dshopping%2520cart%7C1615429250675%3B; s_sq=%5B%5BB%5D%5D' --data-binary '{"ItemList":[{"ItemNumber":"33-320-424","ItemKey":"eyJTYWxlVHlwZSI6MSwiSXRlbUdyb3VwIjoxLCJJdGVtTnVtYmVyIjoiMzMtMzIwLTQyNCIsIk9wdGlvbmFsSW5mb3MiOltdfQ==","Quantity":1,"ItemGroup":"Single"}],"Actions":[]}' 'https://secure.newegg.com/shop/api/CheckoutApi' -o testing.txt"""
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
    autoChrome.get('https://newegg.com')
    autoChrome.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[4]/div[1]/div[1]/a').click()
    login_field = autoChrome.find_element_by_xpath('//*[@id="labeled-input-signEmail"]')
    current_url = autoChrome.current_url
    #wait for URL to change with 10 second timeout
    #WebDriverWait(autoChrome, 1000).until(EC.url_changes(current_url))

    login_field.send_keys(login)
    print(autoChrome.title)
    autoChrome.find_element_by_id('signInSubmit').click()
    print("username input successful")

#connect to email, parse most recent email from Newegg(containing ver code)
#   and extract and return ver code
def retrieve_ver_code():
    return 0


#parse response from within curl output file-- checkout_response
#   in order to obtain sessionId used for final checkout url
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

#use formatting to build custom string for curl command to Checkout API
def build_checkout_request(key):
    str = """curl -s -k -X 'POST' -H 'Host: secure.newegg.com' -H 'Connection: close' -H 'Content-Length: 210' -H 'Accept: application/json, text/plain, */*' -H 'X-Requested-With: XMLHttpRequest' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://secure.newegg.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Referer: https://secure.newegg.com/shop/cart' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9'"""

    dump_cookies()
    cookies_list = load_cookies()


    cookies = " -b " +  extract_cookies(cookies_list)
    print("COOKIES FOR CHECKOUT_REQUEST")
    print(cookies)

    payload = ' --data-binary \'{"ItemList":[{"ItemNumber":"' + item_number_str + '","ItemKey":"' + key + '","Quantity":1,"ItemGroup":"Single"}],"Actions":[]}\''

    target = """ 'https://secure.newegg.com/shop/api/CheckoutApi' -o 'testing.txt'"""
    cmd = str + cookies + payload + target

    print(cmd)
    return cmd

def build_checkout_url(session_id):
    base_url = 'https://secure.newegg.com/shop/checkout?sessionId='
    return(base_url + session_id)

autoChrome = webdriver.Chrome('./chromedriver',chrome_options=options)

sign_in()

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
        #print('From:' + email_message['From'])
        #print('To:' + email_message['To'])
        #print('Date:' + email_message['Date'])
        #print('Subject:' + str(email_message['Subject']))
            #print('Content:' + str(email_message.get_payload(decode=True)))
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
time.sleep(5)
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

#command = build_checkout_request(key)

#os.system(curl_cmd)
#os.system(command)
os.system(cmd)
time.sleep(3)

session_id = retrieve_Session_ID()

#get secure checkout page utilizing Session_ID in url
checkout_url = build_checkout_url(session_id)
print("CHECKOUT URL: ")
print(checkout_url)
autoChrome.get(checkout_url)

time.sleep(3)

cvv_field = autoChrome.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/input')
cvv_field.click()
cvv_field.send_keys(cvv)
#autoChrome.execute_script("arguments[0].value = '732'", cvv_field)

#time.sleep(2)

############BUY ITEM###############
#autoChrome.find_element_by_xpath('//*[@id="btnCreditCard"]').click()
#print(checkout_response.text)
#print(checkout_response.status_code)

#clean up webdriver instance
autoChrome.close()
autoChrome.quit()
