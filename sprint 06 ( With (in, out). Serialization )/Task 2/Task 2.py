import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def unpack_json(file):
    try:
        with open(file) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        logging.error(f"File {file} doesn't exists")


def parse_user(output_file, *args):
    data = []
    for items in args:
        json = unpack_json(items)
        if json != None:
            for item in json:
                if "name" in item.keys():
                    repeated = 0
                    if len(data) > 0:
                        for items in data:
                            if item["name"] == items["name"]:
                                repeated += 1
                    if repeated == 0:
                        data.append(item)
    return create_json(output_file, data)


def create_json(file, data):
    with open(file, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return file


print(parse_user('user3.json' , 'user1.json', 'user2.json'))
