import json
import datetime

with open("./data-2.json", "r") as f:
    data2 = json.load(f)

data2["deviceID"] = data2["device"]["id"]
data2["deviceType"] = data2["device"]["type"]

date = datetime.datetime.strptime(data2["timestamp"], '%Y-%m-%dT%H:%M:%S.%fZ')
timestamp = (date - datetime.datetime(1970, 1, 1)).total_seconds()*1000
del data2["timestamp"]
data2["timestamp"] = timestamp[:-2]

data2["location"] = {"country": data2["country"], "city": data2["city"], "area": data2["area"], "factory": data2["factory"], "section": data2["section"]}

del data2["device"], data2["country"], data2["city"], data2["area"], data2["factory"], data2["section"]

data2["data2"] = data2["data"]
del data2["data"]

data2["data"] = data2["data2"]
del data2["data2"]

print(data2)


