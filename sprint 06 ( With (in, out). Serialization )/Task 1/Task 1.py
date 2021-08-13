import json


def find(file, key):
    result = []
    with open(file, 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            for x in data:
                for item, value in x.items():
                    if isinstance(value, dict):
                        data.append(value)
                    if item == key:
                        if isinstance(value, list) and value not in result:
                            for j in value:
                                if j in result:
                                    result.remove(j)
                            result.extend(value)
                        if value not in result and not isinstance(value, list):
                            result.append(value)
        else:
            if key in data.keys():
                if type(data[key]) is not list and data[key] not in result:
                    result.append(data[key])
                else:
                    for item in data[key]:
                        if item not in result:
                            result.append(item)
        return result


print((find('1.json', 'password')))
print((find('2.json', 'password')))
print((find('3.json', 'password')))
