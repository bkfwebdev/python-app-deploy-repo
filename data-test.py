import pprint
import json

with open('philly_data.json') as json_file:
    data = json.load(json_file)

data_array = data["results"]["data"]

#print(len(data_array))

#print(data_array)

#what_is_this = data_array.pop(31)

#print(what_is_this)

for data_point in data_array:
    if "name" in data_point:
        print(data_point["name"])
    if "phone" in data_point:
        print(data_point["phone"])
    if "website" in data_point:
        print(data_point["website"])
    if "address" in data_point:
        print(data_point["address"])
