import json, unittest, datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    jsonData1 = jsonObject
    loc = jsonData1["location"].split("/")
    jsonData1["location"] = {"country": loc[0], "city": loc[1], "area": loc[2], "factory": loc[3], "section": loc[4]}

    jsonData1["data"] = {"status": jsonData1["operationStatus"],"temperature":     jsonData1["temp"]}
    del jsonData1["operationStatus"]
    del jsonData1["temp"]

    with open('./data-1-conv.json', 'w') as datafile1:
        json.dump(jsonData1,datafile1)
    with open("./data-1-conv.json", "r") as data1:
        d1 = json.load(data1)
    return d1


def convertFromFormat2(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    data2 = jsonObject
    data2["deviceID"] = data2["device"]["id"]
    data2["deviceType"] = data2["device"]["type"]

    date = datetime.datetime.strptime(data2["timestamp"], '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = str((date - datetime.datetime(1970, 1, 1)).total_seconds()*1000)
    del data2["timestamp"]
    data2["timestamp"] = int(timestamp[:-2])

    data2["location"] = {"country": data2["country"], "city": data2["city"], "area": data2["area"], "factory": data2["factory"], "section": data2["section"]}

    del data2["device"], data2["country"], data2["city"], data2["area"], data2["factory"], data2["section"]

    data2["data2"] = data2["data"]
    del data2["data"]

    data2["data"] = data2["data2"]
    del data2["data2"]

    with open('./data-2-conv.json', 'w') as datafile2:
        json.dump(data2,datafile2)
    with open("./data-2-conv.json", "r") as data2:
        d2 = json.load(data2)
    
    return d2


def main(jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):
    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):

        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 1 failed')

    def test_dataType2(self):

        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 2 failed')


if __name__ == '__main__':
    unittest.main()
