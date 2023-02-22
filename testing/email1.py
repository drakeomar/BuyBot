"""curl -i -s -k -X 'POST' -H 'Host: secure.newegg.com' -H 'Connection: close' -H 'Content-Length: 210' -H 'Accept: application/json, text/plain, */*' -H 'X-Requested-With: XMLHttpRequest' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://secure.newegg.com' -H $'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Referer: https://secure.newegg.com/shop/cart' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -b 'NVTC=248326808.0001.00ti2lru0.1615340499.1615340499.1615340499.1; NSC_mc-tfdvsf.ofxfhh.dpn-ttm=475ca3dd1d9fd9ecad9e7b571e24c269f8853bce0bb7a79366da926cd742e504f1ea5f00; NV%5FW57=USA; NV%5FW62=en; usprivacy=1YNY; _ga=GA1.2.1675680289.1615340507; _gid=GA1.2.211558870.1615340507; _gat=1; _cc=AYjdHfRbEYufz1QoDbSRsuPm; s_ecid=MCMID%7C64195341773908164166426898819056776727; AMCVS_1E15776A524450BC0A490D44%40AdobeOrg=1; s_cc=true; NID=72725z2Q72344M5z721cef954f0e7e1413b52bf91eff4d03c5b; NV%5FSPT=; NV%5FCARTOTHERINFO=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22ct1%22%3a%220%22%7d%2c%22Exp%22%3a%221615426922%22%7d%7d%7d; NV%5FCUSTOMERLOGIN=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22sj%22%3a%220%22%2c%22sb%22%3a%22NdTZGLsi966F0Uw94FVBpgigavOcGLusp2w6cnDEUsqKw30kUgLJ792Rae0Ka13DTIP7VwdJAnw%253d%22%2c%22sd%22%3a%22drake%2540wirecutcompany.com%22%2c%22sc%22%3a%2280750583%22%2c%22si%22%3a%22Drake%2bOmar%22%7d%2c%22Exp%22%3a%222562025322%22%7d%7d%7d; NV%5FOTHERINFO=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22sb%22%3a%22NdTZGLsi966F0Uw94FVBpgigavOcGLusp2w6cnDEUsqKw30kUgLJ792Rae0Ka13DTIP7VwdJAnw%253d%22%2c%22sd%22%3a%22NdTZGLsi966F0Uw94FVBpgigavOcGLusp2w6cnDEUsqKw30kUgLJ792Rae0Ka13DTIP7VwdJAnw%253d%22%2c%22sc%22%3a%22WIhJrLSe0yzXwKdSJwU0JPBreL%252fEOp%252fA%22%2c%22si%22%3a%22Drake%2bOmar%22%2c%22s115%22%3a%220nNMDJV3VOjhhOc68MAw6Q%253d%253d%22%2c%22sn%22%3a%224406617224877620210309174202%22%7d%2c%22Exp%22%3a%222562025322%22%7d%7d%7d; NV%5FDVINFO=#5%7b%22Sites%22%3a%7b%22USA%22%3a%7b%22Values%22%3a%7b%22w19%22%3a%22Y%22%2c%22s81%22%3a%2280750583%22%7d%2c%22Exp%22%3a%221615426902%22%7d%7d%7d; NV%5FTOKEN=VM47j51UVJzWSByasaTLtdM3fMFKMq3gydm8KAPWe%2bpRtmc1IjRltzBDL%2beJh%2fXB5TeyJh1bGzFrFWxmHCr%2b97nm4%2beLCYJkaO%2fhii3IvJRDZUJoDRWgm%2b%2fIyc3kOqil48VfHlHvVJkytB2iG%2b2gdHqakwU%2b6pKdHKWAU%2fQvDSRXrodSJ3K0UPfjLemlkEXxziBRR0OiRsnt5FbW70EiaA%3d%3d; NV%5FS115=0nNMDJV3VOjhhOc68MAw6Q%3d%3d; NV%5FCONFIGURATION=#5%7B%22Sites%22%3A%7B%22USA%22%3A%7B%22Values%22%3A%7B%22w58%22%3A%22USD%22%2C%22w61%22%3A%221646876502212%22%2C%22w57%22%3A%22USA%22%7D%2C%22Exp%22%3A86400000000%7D%7D%7D; mt.v=2.41737223.1615340525812; mt.sc=%7B%22i%22%3A1615340526221%2C%22d%22%3A%5B%5D%7D; s_sess=%20s_cpc%3D0%3B; AMCV_1E15776A524450BC0A490D44%40AdobeOrg=870038026%7CMCIDTS%7C18697%7CMCMID%7C64195341773908164166426898819056776727%7CMCAID%7CNONE%7CMCOPTOUT-1615347726s%7CNONE%7CvVersion%7C5.0.0%7CMCAAMLH-1615945326%7C9%7CMCAAMB-1615945326%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18704; _gcl_au=1.1.1954403200.1615340528; _fbp=fb.1.1615340531081.852631568; __gads=ID=756891548cd46333:T=1615340531:S=ALNI_MbQzlhuTRf5NeRI-yJ_8AhBp7F2nQ; NV%5FPREVIOUSSERVERNAME=#5%7B%22Sites%22%3A%7B%22USA%22%3A%7B%22Values%22%3A%7B%22sr%22%3A%22E11%22%7D%2C%22Exp%22%3A0%7D%7D%7D; NV%5FLASTTICK=ko2GSzzd_2mH8GlnMYgVWQ; OptanonConsent=isIABGlobal=false&datestamp=Tue+Mar+09+2021+17%3A42%3A19+GMT-0800+(Pacific+Standard+Time)&version=6.6.0&hosts=&consentId=33af735d-541a-4533-8ae0-3ec64f635f88&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CBG2%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false; mt.visits=%7B%22lastVisit%22%3A1615340540048%2C%22visits%22%3A%5B1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%5D%7D; _uetsid=d258d350814111ebaf8793266602c776; _uetvid=d258ffa0814111ebaec225eae711b0b3; mp_newegg_mixpanel=%7B%22distinct_id%22%3A%20%2217819cc136211a-0958263d9d1576-53e3566-1fa400-17819cc1363146%22%2C%22bc_persist_updated%22%3A%201615340540484%2C%22customer_country%22%3A%20%22US%22%2C%22bc_id%22%3A%20-1719187002%7D; NV_NVTCTIMESTAMP=1615340541; stc118799=tsa:1615340527629.335375817.1285734.4226382475201367.8:20210310021221|env:1%7C20210410014207%7C20210310021221%7C2%7C1083032:20220310014221|uid:1615340527628.1034276269.3901258.118799.1098129919:20220310014221|srchist:1083032%3A1%3A20210410014207:20220310014221; xyz_cr_100393_et_137==NaN&cr=100393&wegc=&et=137&ap=; s_pers=%20productnum%3D1%7C1617932526288%3B%20s_vs%3D1%7C1615342358347%3B%20gpv_pv%3Dshopping%2520cart%7C1615342358352%3B%20s_nr%3D1615340558358-New%7C1646876558358%3B%20gpvch%3Dshopping%2520cart%7C1615342358360%3B; s_sq=%5B%5BB%5D%5D' --data-binary '{"ItemList":[{"ItemNumber":"9SIA8C68VE4920","ItemKey":"eyJTYWxlVHlwZSI6MSwiSXRlbUdyb3VwIjoxLCJJdGVtTnVtYmVyIjoiOVNJQThDNjhWRTQ5MjAiLCJPcHRpb25hbEluZm9zIjpbXX0=","Quantity":1,"ItemGroup":"Single"}],"Actions":[]}' 'https://secure.newegg.com/shop/api/CheckoutApi' -o 'test.txt'"""


tid%3Adf5644ab-835a-11eb-9088-005056ae0065

curl -i -L -s -k -X $'GET' \
    -H $'Host: www.bestbuy.com' -H $'Connection: close' -H $'sec-ch-ua: \";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"' -H $'sec-ch-ua-mobile: ?0' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-Dest: document' -H $'Referer: https://www.bestbuy.com/cart' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' \
    -b $'UID=e9ae724b-bb26-4583-aa02-6415b9ac90a6; physical_dma=803; oid=885290658; vt=d689ab7a-8354-11eb-8a78-06b03c3b6223; bm_sz=4F5A5A73D1E92B8653E3413D0E0CF4F8~YAAQpiMduBCnOx94AQAAs21kJwsHzn05ScUn7LH5Nu+PH0i5y1SN0wiHrTk2drna3mysPYp5FpOfIirURSO2B3gqkkpfWNmN3Ar+dkW0XGMGISnF4+LfhiMTUXhkHTSWX02Q9PiT7IFh4sGcP1opMVFmDAMqETyCxEQ9QAtNl00sJC4BBDPo4zFYzFHdQp6Q6wxoF9rzxsxNHx/oxBRUefK8Znq4E8Ndi9I2cMx47ZXoZ3JtmSm0W1z+ZyA1u1NLmd+D34glUMzx2Qt2J5+W9Uv/DacOZCfii2sWrg==; bby_rdp=l; CTT=ab546b0442e0f18dd007f1e618c2c48f; SID=2eba9787-66a6-4989-830b-0c4f30643d4b; rxVisitor=1615568600225D2QQLER1VSJ62AR01464HDMM8JEH0NRM; optimizelyEndUserId=oeu1615568600372r0.8796325170603911; COM_TEST_FIX=2021-03-12T17%3A03%3A20.861Z; c6db37d7c8add47f1af93cf219c2c682=6884d139498e54c39431f7cf0e22cd89; AMCVS_F6301253512D2BDB0A490D45%40AdobeOrg=1; __gads=ID=23f859bba5fe46b2:T=1615568606:S=ALNI_MY5ZJThfcA4Z823PXwCU3bO6wJr7A; s_ecid=MCMID%7C70602062113183112280757020245676280257; _cs_mk=0.10979817802663927_1615568609676; s_cc=true; 52245=; _cs_c=1; _gcl_au=1.1.2040905216.1615568612; analyticsStoreId=117; locStoreId=117; aam_uuid=75549181758081761580262312474081124579; customerZipCode=90703|Y; pst2=117; CTE2=T; CTE3=T; CTE30=F; ZPLANK=7d4483643a9c43438686c84482cf1e1a; ui=1615570108413; dtCookie=v_4_srv_7_sn_5R0L8ROKK7NCMPBAFI7PUS26ORVU4RPS_app-3Aea7c4b59f27d43eb_1_app-3A1531b71cca36e130_1_app-3A1b02c17e3de73d2a_1_app-3A21f5a3c46dc908d0_1_ol_0_perc_100000_mul_1; G_ENABLED_IDPS=google; pt=3457321985; locDestZip=92646; DYN_USER_CONFIRM=261f2786a4fe6a48bf2ad6295593f65b; DYN_USER_ID=ATG49434271481; ut=13245fd5-8299-11eb-9f49-0656f9a9ca8f; at=eyJhY2Nlc3NUb2tlbiI6IllXTXRkZUl1ZVlOWUVldXhJQW91Ml9uV05Rb05xLXdTZTh1SFh6aW1rRlIxTHBBQVp1OHlBQUFBQUFBQUFBQSIsInRpbWVUb0xpdmUiOjE4MDAsImlzc3VlZFRpbWVzdGFtcCI6MTYxNTU3MDE1MjMwNSwiYXNzZXJ0aW9uIjoidTp5ckVubm1DckktS3RZZ3RaQWdSeUMwbzZja21WcDcxYW5WQkRxbTgzTTg4IiwicHJpbmNpcGFsIjoidTp5ckVubm1DckktS3RZZ3RaQWdSeUMwbzZja21WcDcxYW5WQkRxbTgzTTg4IiwicHJpbmNpcGFsSWRlbnRpZmllciI6IjEzMjQ1ZmQ1LTgyOTktMTFlYi05ZjQ5LTA2NTZmOWE5Y2E4ZiIsImNvbnN1bWFibGUiOmZhbHNlLCJ2ZXJzaW9uIjoiMS4wIn0.AIjZiZqP58MwRH0MRc3ok3XrvUYtBp3HNX3Fgwco7KN-2kJyD9G6XoPi5GTH72ffMKa9H4jWTeGYkTWsTfGXLg; analyticsToken=13245fd5-8299-11eb-9f49-0656f9a9ca8f; AMCV_F6301253512D2BDB0A490D45%40AdobeOrg=1585540135%7CMCMID%7C70602062113183112280757020245676280257%7CMCAAMLH-1616174965%7C9%7CMCAAMB-1616174965%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615577365s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C1115001316%7CvVersion%7C4.4.0; cst_lb=p-cart-cloud; ltc=10130; bby_cbc_lb=p-browse-w; bby_loc_lb=p-loc-w; bby_prc_lb=p-prc-w; bby_idn_lb=p-idn-cloud; bby_txco_lb=p-txco-cloud; PAYMENT_SECTKN=692c0e97-8816-47b0-819b-ab7c6a449e1f; SECTKN=Z+F7iVuR+EJmVhrBGIb37p5fHEb+akUWCFso64ToFvVDLZB3Q+OxfaBSG/3YPbuObLZMb0ZTYveRs0WqT8L3Ei49zoz0B4hHBvsU48mmGl09qw2uNGhkokt0qJCI+1ru837JV9l9mQMQSUFBwmVoBQ; sc-location-v2=%7B%22meta%22%3A%7B%22CreatedAt%22%3A%222021-03-12T17%3A03%3A37.773Z%22%2C%22ModifiedAt%22%3A%222021-03-12T17%3A46%3A02.143Z%22%2C%22ExpiresAt%22%3A%222022-03-12T17%3A46%3A02.143Z%22%7D%2C%22value%22%3A%22%7B%5C%22physical%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2290637%5C%22%2C%5C%22source%5C%22%3A%5C%22A%5C%22%2C%5C%22captureTime%5C%22%3A%5C%222021-03-12T17%3A29%3A23.879Z%5C%22%7D%2C%5C%22store%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2290703%5C%22%2C%5C%22searchZipCode%5C%22%3A%5C%2290637%5C%22%2C%5C%22storeId%5C%22%3A%5C%22117%5C%22%2C%5C%22storeHydratedCaptureTime%5C%22%3A%5C%222021-03-12T17%3A29%3A24.884Z%5C%22%2C%5C%22userToken%5C%22%3A%5C%2213245fd5-8299-11eb-9f49-0656f9a9ca8f%5C%22%7D%2C%5C%22destination%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2292646%5C%22%7D%7D%22%7D; rxvt=1615572964102|1615568600228; dtPC=7$371163638_45h-vAQQTKHUDCBRGWHPGHGFTQAKHSBAFUMMB-0e15; CartItemCount=1; c2=Checkout%3A%20Cart%20-%20Index; _abck=9C7BAEEF5A07495F3E7235CE92F0F109~-1~YAAQhyMduM0QcRJ4AQAAo6+LJwXiZ7ZexIt4Y+i6ihFsbeF8HZVosvgWbz9ovClJJ/shXNiRurTmVrd6lTRlnxaKRmQ7Omt/myFPvlZ0m3lhRomK6oca+V1GvIi+MO+5Au0BKJ+CA4Ci7IBrhJuveN8lLvOem8mIw97d1FZNtQKZW05XyXbM1nnbfUkTGMZ7reQ6QWn8+7RgqIiW/BwgB69YQVoAswrSqflNwgtBzjPQ+Uc/Jp5CVyydzS547ai1Tyd0tP4k0qLbTxkbc/YwSYbyQsxlzJR/bwabzMwitSrfZvbxHRlXG388liaoW9yQxUW2wDFRwofmpnU63mpzMw3P/t5+hBtslMrVRzKUVX8p1XtDrBycSU7VmVUNIaxPl7BFVgqDrIw9ckX8eMDPczyEkyGs+R1F+4BnMdwcNA+iANqb1A==~-1~-1~-1; _cs_id=92400119-6a25-acd2-9123-6b20063bc2d4.1615568612.1.1615571169.1615568612.1614089558.1649732612037.Lax.0; _cs_s=7.1; dtLatC=29; s_sq=%5B%5BB%5D%5D; basketTimestamp=1615571187722; dtSa=-' \
    $'https://www.bestbuy.com/identity/signin?token=tid%3Adf5644ab-835a-11eb-9088-005056ae0065'
