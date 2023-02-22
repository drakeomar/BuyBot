from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import pickle
import json
import time
import imaplib, email
import html2text

null = None #to post to /cart/checkout

sku_str = "6394025"

user = 'drake@wirecutcompany.com'
password = 'JanuarySTG@041288'
imap_url = 'imap.gmail.com'

bb_user = "drake@wirecutcompany.com"
bb_password = "JanuarySTG@041288"
bb_reset_password = "TheworstofDecember21"

checkout_url_code = "6f8d9300-839f-11eb-88a2-773cf5b4f234"
payment_ref_id = "f7981e10-8696-11eb-87d2-d35987fa68ae"
credit_card_profile_id = "6918b27517e746ae66a7d929f96a75e6cb6da868"

#headers_dict = {''}
def sign_in():
    return 0

autoChrome = webdriver.Chrome('./chromedriver')

s = requests.Session()
s.get("https://www.bestbuy.com")
#s.get('https://www.bestbuy.com')
#print(s.cookies)

#s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})
#signin_response = s.get('https://www.bestbuy.com/identity/global/signin')
#print(s.headers)

#print(signin_response.text)
#print(signin_response.status_code)

#autoChrome.get('https://www.bestbuy.com')
#autoChrome.get('https://www.bestbuy.com')
autoChrome.get('https://www.bestbuy.com/identity/global/signin')
current_url = autoChrome.current_url
print(current_url)
autoChrome.find_element_by_xpath('//*[@id="fld-e"]').send_keys(bb_user)
autoChrome.find_element_by_xpath('//*[@id="fld-p1"]').send_keys(bb_reset_password)
autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button').click()
time.sleep(3)
#autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/span/a').click()
#autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/button').click()
#time.sleep(5)

#print("TITLE: ")
#print(autoChrome.title)

#if autoChrome.title == "Sign In - One Time Sign In Link or Reset Password - Best Buy":
    #autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/button[2]').click()


dad = '''
connection = imaplib.IMAP4_SSL(imap_url)
connection.login(user, password)
connection.select('Inbox')


result, data = connection.uid('search', None, '(FROM "BestBuyInfo@emailinfo.bestbuy.com")')
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
        result = output.find("Verification Code:")


            #print(output)
            #print(result)
        result = result + 20
        end_result = result + 10
        verification_code = output[result:end_result].strip()

        print("Done")

connection.close()
connection.logout()

ver_field = autoChrome.find_element_by_xpath('//*[@id="verificationCode"]')
ver_field.click()
ver_field.clear()
ver_field.send_keys(verification_code)

#print(verification_code)
#ver_field.send_keys(verification_code[0])
#ver_field.send_keys(verification_code[1])
#ver_field.send_keys(verification_code[2])
#ver_field.send_keys(verification_code[3])
#ver_field.send_keys(verification_code[4])
#ver_field.send_keys(verification_code[5])

autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/button').click()

time.sleep(3)
p1 = autoChrome.find_element_by_xpath('//*[@id="fld-p1"]')
p2 = autoChrome.find_element_by_xpath('//*[@id="reenterPassword"]')

p1.click()
p1.send_keys(bb_reset_password)

p2.click()
p2.send_keys(bb_reset_password)

autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[5]/button').click()

'''
def dump_cookies():
    pickle.dump(autoChrome.get_cookies(), open("bestbuy_cookies.pk1","wb"))


#returns a list of dict objects that are each individual cooki
def load_cookies():
    return pickle.load(open("bestbuy_cookies.pk1","rb"))

def update_cookies(cookies_list):
    for cookie in cookies_list:
        cookie_name = cookie["name"]
        cookie_value = cookie["value"]
        cookie_domain = cookie["domain"]
        #print(cookie_name + ": " + cookie_value + ", " + cookie_domain)
        if cookie_name == "UID" or cookie_name == "ut" or cookie_name == "bm_sz":
            s.cookies.set(cookie_name, cookie_value, domain=cookie_domain)

#bm_sz cookie required
#ut cookie required -- ALWAYS THE SAME FOR THIS ACCOUNT, PULL AFTER LOGIN THO OR HARDCODE IF NECESSARY
def add_to_cart():
    dump_cookies()
    cookies = load_cookies()
    #print(cookies)
    update_cookies(cookies)

    #print(s.headers)

    headers = {'Host':'www.bestbuy.com',  'Accept':'application/json', 'Content-Type':'application/json; charset=UTF-8', 'Origin':'https://www.bestbuy.com', 'User-Agent':'";Not A Brand";v="99", "Chromium";v="88"', 'Accept-Encoding':'identity', 'Accept-Language':'en-US,en;q=0.9' }
    s.headers.update(headers)
    print(s.headers)
    print(s.cookies)
    response = s.post('https://www.bestbuy.com/cart/api/v1/addToCart', json={"items":[{"skuId":sku_str}]})

    print(response.text)
    #print(s.headers)

def checkout():
    checkout_response = s.post('https://www.bestbuy.com/cart/checkout', json=null)
    #print(checkout_response.text)
    checkout_object = json.loads(checkout_response.text)
    #print(checkout_object)
    autoChrome.get(checkout_object["updateData"]['redirectUrl'])

    cvv_field = autoChrome.find_element_by_xpath('//*[@id="credit-card-cvv"]')
    cvv_field.click()
    cvv_field.clear()
    cvv_field.send_keys("732")

    print(autoChrome.current_url)

time.sleep(3)

add_to_cart()
checkout()
