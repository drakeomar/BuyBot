import requests

s = requests.Session()
s.cookies.set("NV%5FW62","en",domain=".newegg.com")
s.cookies.set("NV%5FCUSTOMERLOGIN","#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22sj%22%3a%220%22%2c%22sb%22%3a%22NdTZGLsi964M39wmy7%252bepKzJhxiIHu0c2zwlRmVz2YWgAJjbVv4q69ftrl0ue940%22%2c%22sd%22%3a%22drakeomar%2540icloud.com%22%2c%22sc%22%3a%2237455212%22%2c%22si%22%3a%22Drake%2bOmar%22%7d%2c%22Exp%22%3a%222561997713%22%7d%7d%7d",domain=".newegg.com")
s.cookies.set("INGRESSCOOKIE","1615310217.653.3309.865907",domain=".newegg.com")

reponse = s.get("https://www.newegg.com")
autologin_response = s.get('https://www.newegg.com/d/dynamic-js/home/Home/USA/initial-json')
null = None
add2cart_response = s.post('https://www.newegg.com/api/Add2Cart',json={"ItemList":[{"ItemGroup":"Single","ItemNumber":"9SIA8C68VE4920","Quantity":1,"OptionalInfos":null,"SaleType":"Sales"}],"CustomerNumber":"Cyw4XhheKD4vi4LDwVl323OZ9SFPrAoE"})

print(add2cart_response.text)
print(s.cookies)
print(add2cart_response.status_code)
print(autologin_response.cookies)
