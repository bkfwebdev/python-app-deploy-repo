import json

with open('philly_data.json') as json_file:
    data = json.load(json_file)

print(data["results"]["data"][0]["location_id"])
print(data["results"]["data"][1]["location_id"])
print(data["results"]["data"][2]["location_id"])
print(data["results"]["data"][3]["location_id"])
print(data["results"]["data"][4]["location_id"])