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
    if data_point["name"]:
        print(data_point["name"])
    if data_point["phone"]:
        print(data_point["phone"])
    if data_point["website"]:
        print(data_point["website"])
    if data_point["address"]:
        print(data_point["address"])
