import json
with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)

loc = jsonData1["location"].split("/")
jsonData1["location"] = {"country": loc[0], "city": loc[1], "area": loc[2], "factory": loc[3], "section": loc[4]}

jsonData1["data"] = {"status": jsonData1["operationStatus"],"temperature": jsonData1["temp"]}
del jsonData1["operationStatus"]
del jsonData1["temp"]

json.dumps(jsonData1)



