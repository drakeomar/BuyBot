from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

#options.add_argument('--window-size=1920,1080')
#options.add_argument('--start-maximized')

autoChrome = webdriver.Firefox(executable_path='/home/drake/pytest/geckodriver', firefox_options=options)
autoChrome.get('https://www.bestbuy.com')
print(autoChrome.get_cookies())
autoChrome.close()
autoChrome.quit()