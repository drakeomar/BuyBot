import requests

for i in range(0,10):
    response = requests.get("https://api.bestbuy.com/click/-/5938403/cart")
    print(response.text)
    response = requests.get("https://api.bestbuy.com/click/-/6426149/cart")
    print(response.text)
    print(response.status_code)
