from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
#options.add_argument('--disable-extensions')
options.add_argument("--no-proxy-server")
options.add_argument("--window-size=1920, 1080")
options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')
#options.add_experimental_option("excludeSwitches",["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)


#autoChrome = webdriver.Chrome('./chromedriver', chrome_options=options)

#autoChrome.get("https://www.bestbuy.com")

bb_user = "drake@wirecutcompany.com"
bb_reset_password = "JanuarySTG@041288"
#binary = FirefoxBinary('/usr/lib/firefox/firefox')
autoFox = webdriver.Firefox(executable_path='/home/drake/pytest/geckodriver', firefox_options=options)


def sign_in():
    autoFox.get('https://www.bestbuy.com/identity/global/signin')
    print(autoFox.page_source)
    autoFox.find_element_by_xpath('//*[@id="fld-e"]').send_keys(bb_user)
    autoFox.find_element_by_xpath('//*[@id="fld-p1"]').send_keys(bb_reset_password)
    autoFox.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button').click()
    print("SIGNED IN")

print("INIT SUCCESS")
sign_in()

time.sleep(5)
print(autoFox.title)
