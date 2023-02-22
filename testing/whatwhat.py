import requests 
import json
import time 

sku = "6426149"
headers = {'Host': 'www.bestbuy.com', 'Connection': 'close','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Accept':'*/*','Accept-Encoding': 'Identity','Accept-Language': 'en-US,en;q=0.9'}
proxy = {'http': 'http://user-sp412c491a:wirecut2021@us.smartproxy.com:10000',
         'https': 'http://user-sp412c491a:wirecut2021@us.smartproxy.com:10000'}

def refresh_session():

    response = requests.get('https://www.bestbuy.com/', headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})

    bm_sz = response.cookies.get_dict()["bm_sz"]

    cookies = {'bm_sz':bm_sz}
    with open('sensor_data.json','rb') as f: 
        sensor_data = json.load(f)

    with open('sensor_data_2.json','rb') as g: 
        sensor_data_2 = json.load(g)

    response = requests.post('https://www.bestbuy.com/resource/35f36a4498rn222844b00247c029f660', headers=headers, cookies=cookies, json=sensor_data)


    print(response.status_code)

    response = requests.post('https://www.bestbuy.com/resource/35f36a4498rn222844b00247c029f660', headers=headers, cookies=cookies, json=sensor_data_2)

    print(response.status_code)
    print(bm_sz)
    return bm_sz 

cookies = {'bm_sz':refresh_session()}
time.sleep(3)
response = requests.post('https://www.bestbuy.com/cart/api/v1/addToCart', headers=headers, cookies=cookies, json={"items":[{"skuId":sku}]}, proxies=proxy)