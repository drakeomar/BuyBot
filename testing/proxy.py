import requests

proxies = { 'http':'http://51.75.147.41:3128','https':'https://51.75.147.41:3128'}

response = requests.get('https://www.bestbuy.com', proxies=proxies)
