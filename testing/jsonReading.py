import json

with open('itemNumbers.json') as f:
    data = json.load(f)
    #print(data["gpus"])
print(data["gpus"]["3080"])
print(data["gpus"]["3080"][0]["item_number"])
print(data["gpus"]["3080"][0]["url"])

for item in data["gpus"]["3080"]:
    print(item["url"])
    print("SEP")
