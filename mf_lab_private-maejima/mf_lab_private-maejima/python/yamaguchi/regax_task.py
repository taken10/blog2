import re
import json


data = [{"term": "2016-12-31T15:00:00.000Z", "tokyo": 7.4, "sooya": -1, "yonaguni": 22.6},
        {"term": "2017-01-01T15:00:00.000Z", "tokyo": 7.2, "sooya": -1.8, "yonaguni": 23},
        {"term": "2017-01-02T15:00:00.000Z", "tokyo": 8, "sooya": -2.4, "yonaguni": 22.1},
        {"term": "2017-01-03T15:00:00.000Z", "tokyo": 8.5, "sooya": -3.5, "yonaguni": 22.1},
        {"term": "2017-01-04T15:00:00.000Z", "tokyo": 6.7, "sooya": -5.7, "yonaguni": 22.3},
        {"term": "2017-01-05T15:00:00.000Z", "tokyo": 4.5, "sooya": -2.3, "yonaguni": 22.8},
        {"term": "2017-01-06T15:00:00.000Z", "tokyo": 4.1, "sooya": -1.5, "yonaguni": 22.9}]

mod_data_array = []
value = ''
sp_value = []
for i in range(len(data)):
        value = re.search("\".*\",?:\s[0-9]{2}\.?[0-9]?", json.dumps(data[i])).group()
        value = value.split(',')
        mod_data_array_1 = []
        print(value)
        for p in range(len(value)):
                sp_value = value[p].split("\":")
                print(sp_value)
                local_value = (sp_value[0].replace('\"', '').strip(), sp_value[1].replace('\"', '').strip())
                mod_data_array_1.append(local_value)
        mod_data_array.append(mod_data_array_1)
print(mod_data_array)
