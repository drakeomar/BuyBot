import requests
import pickle

proxy = {'http': 'http://user-sp412c491a:wirecut2021@us.smartproxy.com:10000',
         'https': 'http://user-sp412c491a:wirecut2021@us.smartproxy.com:10000'}
sku = "9226875"
s = requests.Session()
#print(s.headers)

my_headers = {'Host':'www.bestbuy.com','Connection':'close','Accept':'*/*','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Accept-Encoding':'Identity','Accept-Language':'en-US,en;q=0.9'}
def new_bm_sz(): 
    #headers = {'Host':'www.bestbuy.com',  'Accept':'application/json', 'Content-Type':'application/json; charset=UTF-8', 'Origin':'https://www.bestbuy.com', 'User-Agent':'";Not A Brand";v="99", "Chromium";v="88"', 'Accept-Encoding':'identity', 'Accept-Language':'en-US,en;q=0.9' }
    response = requests.get('https://www.bestbuy.com',headers=my_headers)
    print(response.headers)
    cookie_str = response.cookies['bm_sz']
    print(cookie_str)
    #my_cookies = {'bm_sz': cookie_str}
    s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
    s.cookies.set('bm_sz', cookie_str, domain='.bestbuy.com')
    #s.cookies.set('ut', '13245fd5-8299-11eb-9f49-0656f9a9ca8f', domain='.bestbuy.com')
    #response = s.post('https://www.bestbuy.com/cart/api/v1/addToCart', json={"items":[{"skuId":sku}]})
    print(response.status_code)
    #print(response.status_code)
    print(response.text)




def get_new_bm_sz():  
    s.headers.update({ 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
    response = s.get('https://www.bestbuy.com')

    cookie_dict = s.cookies.get_dict(domain='.bestbuy.com')

    return cookie_dict['bm_sz']

#while True: 
    #print("NEW BM_SZ = ", end="", flush=True)
    #print(get_new_bm_sz())

new_bm_sz()