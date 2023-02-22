from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
import requests
import pickle
import json
import time
import imaplib, email
import html2text
import string
import random

with open('bb_config.json') as f:
    configData = json.load(f)
    
proxy_list = [ configData["proxy_1"], configData["proxy_2"], configData["proxy_3"], configData["proxy_4"] ]
proxies = { 'https':random.choice(proxy_list) }

null = None #to post to /cart/checkout

sku_str = "6426149"

#email
user = configData["email_user"]
password = configData["password"]
imap_url = configData["imap_url"]

#sign_in
bb_user = configData["bb_user"]
bb_password = configData["bb_password"]
bb_reset_password = configData["bb_reset_password"]

#checkout/account info
checkout_url_code = "6f8d9300-839f-11eb-88a2-773cf5b4f234"
payment_ref_id = "f7981e10-8696-11eb-87d2-d35987fa68ae"
credit_card_profile_id = "6918b27517e746ae66a7d929f96a75e6cb6da868"

#capabilities = DesiredCapabilities.CHROME.copy()
#capabilities['acceptSslCerts'] = True
#capabilities['acceptInsecureCerts'] = True

class Bestbot:

    def __init__(self, bb_user=configData["bb_user"]):
        self.bb_user = bb_user
        
        print("initializing...",end="",flush=True)
        options = Options()
        #options.add_argument("--headless")
        #options.add_argument("--disable-gpu")

        options.add_argument('--window-size=1920,1080')
        options.add_argument('--start-maximized')

        self.autoChrome = webdriver.Firefox(executable_path='/home/drake/pytest/geckodriver', firefox_options=options)
        print(" SUCCESS")

        #self.autoChrome = webdriver.Chrome('./chromedriver', chrome_options=chrome_options, desired_capabilities=capabilities)
        self.s = requests.Session()

    def __del__(self):
        print("DESTRUCTOR CALLED")

        #self.autoChrome.quit()

    def goto_site(self): 
        self.autoChrome.get('https://www.bestbuy.com')

    def sign_in(self):
        print("attempting to sign in...")
        self.autoChrome.get('https://www.bestbuy.com/identity/global/signin')

        self.autoChrome.find_element_by_xpath('//*[@id="fld-e"]').send_keys(self.bb_user)
        self.autoChrome.find_element_by_xpath('//*[@id="fld-p1"]').send_keys(bb_reset_password)
        self.autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button').click()

        time.sleep(3)


    #s.get('https://www.bestbuy.com')
    #print(s.cookies)

    #s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})
    #signin_response = s.get('https://www.bestbuy.com/identity/global/signin')
    #print(s.headers)

    #print(signin_response.text)
    #print(signin_response.status_code)

    #autoChrome.get('https://www.bestbuy.com')
    #autoChrome.get('https://www.bestbuy.com')

    def get_current_url(self):
        return self.autoChrome.current_url


    #autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/span/a').click()
    #autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/button').click()
    #time.sleep(5)

    #print("TITLE: ")
    #print(autoChrome.title)

    #if autoChrome.title == "Sign In - One Time Sign In Link or Reset Password - Best Buy":
        #autoChrome.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/button[2]').click()

    def dump_cookies(self):
        print("writing initial session cookies to file...")
        pickle.dump(self.autoChrome.get_cookies(), open("bestbuy_cookies.pk1","wb"))


    #returns a list of dict objects that are each individual cooki
    def load_cookies(self):
        print("loading cookies from file...")
        return pickle.load(open("bestbuy_cookies.pk1","rb"))

    #update the cookies of requests session to use moving forward and preserve 
    #  sign in
    def update_cookies(self, cookies_list):
        for cookie in cookies_list:
            cookie_name = cookie["name"]
            cookie_value = cookie["value"]
            cookie_domain = cookie["domain"]
            #print(cookie_name + ": " + cookie_value + ", " + cookie_domain)
            if  cookie_name == "ut" or cookie_name == "bm_sz":
                self.s.cookies.set(cookie_name, cookie_value, domain=cookie_domain)

    def refine_checkout_json(self, json_str):

        return 0

    #method that returns the new bm_sz cookie that is required to bypass the 
    #  request limit for adding an item to cart. Method is integral to avoiding 
    #  Best Buy stock trickling anti-bot protection
    def refresh_session(self): 
        print("attempting to refresh session...")
        headers = {'Host': 'www.bestbuy.com', 'Connection': 'close','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Accept':'*/*','Accept-Encoding': 'Identity','Accept-Language': 'en-US,en;q=0.9'}

        response = requests.get('https://www.bestbuy.com/', headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})

        bm_sz = response.cookies.get_dict()["bm_sz"]

        cookies = {'bm_sz':bm_sz}
        with open('sensor_data.json','rb') as f: 
            sensor_data = json.load(f)

        with open('sensor_data_2.json','rb') as g: 
            sensor_data_2 = json.load(g)

        #implement try catch block with these requests
        response = requests.post('https://www.bestbuy.com/resource/35f36a4498rn222844b00247c029f660', headers=headers, cookies=cookies, json=sensor_data)
        print(response.status_code)
        response = requests.post('https://www.bestbuy.com/resource/35f36a4498rn222844b00247c029f660', headers=headers, cookies=cookies, json=sensor_data_2)
        print(response.status_code) 
        return bm_sz

        
    #bm_sz cookie required
    #ut cookie required -- ALWAYS THE SAME FOR THIS ACCOUNT, PULL AFTER LOGIN THO OR HARDCODE IF NECESSARY
    def add_to_cart(self, sku):
        self.dump_cookies()
        cookies = self.load_cookies()
        #print(cookies), chrome_options=chrome_options, desired_capabilities=capabilities)
        self.update_cookies(cookies)

        #print(s.headers)
        print("adding to cart...")
        headers = {'Host':'www.bestbuy.com', 'Accept':'application/json', 'Content-Type':'application/json; charset=UTF-8', 'Origin':'https://www.bestbuy.com', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Accept-Encoding':'Identity', 'Accept-Language':'en-US,en;q=0.9' }
        self.s.headers.update(headers)
        print(self.s.headers)
        print(self.s.cookies)
        status_code = 0
        while status_code != 200:
            #response = requests.get("https://api.bestbuy.com/click/-/6426145/cart")
            #status_code = response.status_code
            
            for i in range(0,4):
                #TODO: setup timeout try catch block to advance to next request
                response = self.s.post('https://www.bestbuy.com/cart/api/v1/addToCart', json={"items":[{"skuId":sku}]}, proxies=proxies)
                status_code = response.status_code
                time.sleep(1)
                print(status_code)
                print(response.text)
                if status_code == 200:
                    break
                if status_code == 500: 
                    break 
            
            bm_sz = self.refresh_session()
            print(bm_sz)
            #ut = self.s.cookies.get_dict()['ut']
            self.s.cookies.clear()
            #self.s.cookies.set('ut',ut,domain='.bestbuy.com')
            self.s.cookies.set('bm_sz',bm_sz,domain='.bestbuy.com')
            print(self.s.cookies)
            #time.sleep(5) 

        print(response.text)
        #print(s.headers)

    #checkout
    def checkout(self, isBuying=False):
        print("checking out...")
        checkout_response = self.s.post('https://www.bestbuy.com/cart/checkout', json=null)
        #print(checkout_response.text)
        checkout_object = json.loads(checkout_response.text)
        #print(checkout_object)
        self.autoChrome.get(checkout_object["updateData"]['redirectUrl'])

        wait = WebDriverWait(self.autoChrome, 10)
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "page-spinner__spinner")))
        #cvv_field = wait.until(ec.visibility_of_element_located((By.ID, "credit-card-cvv")))

        #WebDriverWait(driver, 10).until(lambda driver: self.autoChrome.execute_script('return document.readyState') == 'complete')
        #time.sleep(5)
        cvv_field = self.autoChrome.find_element_by_xpath('//*[@id="credit-card-cvv"]')
        cvv_field.click()
        #cvv_field.clear()
        cvv_field.send_keys("732")
        if isBuying:
            self.autoChrome.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button').click()
            print("IS BUYING")
            time.sleep(3)
        else:
            test_text_file = open("test.txt","w")
            n = test_text_file.write(self.autoChrome.page_source)
            test_text_file.close()
            soup = BeautifulSoup(self.autoChrome.page_source, 'html.parser')
            scripts = soup.find_all("script")
            #print(scripts[7])
            my_list = scripts[7].string.split(";")
            json_object = json.loads(my_list[0][17:])#print first delimited string after first 16 char
            print(json_object)
        print(self.autoChrome.current_url)

    def confirm(self, email, text):
        if email:
            return None
        if text:
            return None


if __name__ == "__main__":

    w = Bestbot()
    w.sign_in()
    w.add_to_cart(sku_str)
    w.checkout(False)
    del w

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

    #print(verification_co, chrome_options=chrome_options, desired_capabilities=capabilities)de)
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
