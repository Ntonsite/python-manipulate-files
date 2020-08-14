import json

with open('C:/Users/nmwamlima/Desktop/remove.json', 'r') as data_file:
    data = json.load(data_file)

for element in data:
    element.pop('data', None)

with open('C:/Users/nmwamlima/Desktop/completeOut.json', 'w') as data_file:
    data = json.dump(data, data_file)