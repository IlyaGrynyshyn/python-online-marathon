import csv
import json

import jsonschema
from jsonschema import validate


def unpack_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data


def validate_json(data, schema, data_type):
    try:
        validate(data, schema)
    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError(data_type)


def user_with_department(csv_file, user_json, department_json):
    schema_user = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required": ["department_id", "name", "id"]
    }

    schema_dep = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["name", "id"]
    }

    user_data = unpack_json(user_json)
    department_data = unpack_json(department_json)
    try:
        with open(csv_file, mode="w") as csv_result:
            headers = {"name": None, "department": None}
            writer = csv.writer(csv_result, delimiter=",")
            writer.writerow(headers.keys())
            for item in user_data:

                validate_json(item, schema_user, "user")

                headers["name"] = item["name"]
                dep_id = item["department_id"]
                dep_id_check = False
                for item in department_data:
                    validate_json(item, schema_dep, "department")
                    if item["id"] == dep_id:
                        headers["department"] = item["name"]
                        writer.writerow(headers.values())
                        dep_id_check = True
                if not dep_id_check:
                    raise DepartmentName(dep_id)
    except DepartmentName as error:
        print(error)
    except InvalidInstanceError as error:
        print(error)


class DepartmentName(Exception):

    def __init__(self, dep_id):
        self.dep_id = dep_id

    def __str__(self):
        return f"Department with id {self.dep_id} doesn't exists"


class InvalidInstanceError(Exception):

    def __init__(self, data_type):
        self.data_type = data_type

    def __str__(self):
        return f'Error in {self.data_type} schema'


try:
    user_with_department("user.csv", "user.json", "department.json")
except DepartmentName as error:
    print(str(error))
