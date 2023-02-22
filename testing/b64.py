#85bac4fac470b1ca2b788057ca4409a1164383303c54fc173dfea745d60c85b1ff70354fc496275d4b6dde78631d83366a56e09a6f15c410dfb5add23ebc7db7
#eyJTYWxlVHlwZSI6MSwiSXRlbUdyb3VwIjoxLCJJdGVtTnVtYmVyIjoiOVNJQThDNjhWRTQ5MjAiLCJPcHRpb25hbEluZm9zIjpbXX0=
#7b3ad68d5ded50060291873ae41fe130cf41d4d26ddfd07f60412fcd66f3eab694716084a3edda5913a182df80c20706c5a7194c27c0ba0799dfad5589d78862
#bb4d37810f86214741feb6af64c54603840a4b307b9d737ed67b7a8ae694ba76bb19ffe8e502cada91ec1af36fcf6e5b
#eyJTYWxlVHlwZSI6MSwiSXRlbUdyb3VwIjoxLCJJdGVtTnVtYmVyIjoiMjAtMTQ3LTc5MCIsIk9wdGlvbmFsSW5mb3MiOltdfQ==
#eyJTYWxlVHlwZSI6MSwiSXRlbUdyb3VwIjoxLCJJdGVtTnVtYmVyIjoiMjAtMTQ3LTc5MCIsIk9wdGlvbmFsSW5mb3MiOltdfQ==

import base64

item_number_str = '9SIA8C68VE4920'

def generate_key():
    str = build_str(item_number_str)
    return base64.b64encode(bytes(str, 'utf-8'))

def build_str(string):
    return '{"SaleType":1,"ItemGroup":1,"ItemNumber":"'+ string + '","OptionalInfos":[]}'

key = generate_key()
print(str(key).replace("b'",""))
