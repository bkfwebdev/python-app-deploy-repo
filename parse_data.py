import json

with open('philly_data.json') as json_file:
    data = json.load(json_file)

#search first enpoint for location id
#seearch second enpoint to ger restauruant info

print(data["results"]["data"][0]["name"])
print(data["results"]["data"][0]["phone"])
print(data["results"]["data"][0]["website"])
print(data["results"]["data"][0]["address"])

print(data["results"]["data"][1]["name"])
print(data["results"]["data"][1]["phone"])
print(data["results"]["data"][1]["website"])
print(data["results"]["data"][1]["address"])

print(data["results"]["data"][2]["name"])
print(data["results"]["data"][2]["phone"])
print(data["results"]["data"][2]["website"])
print(data["results"]["data"][2]["address"])

