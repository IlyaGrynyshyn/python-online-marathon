import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = "JSON"
    BYTE = "BYTE"


class SerializeManager:
    def __init__(self, file_name, filetype):
        self.file_name = file_name
        self.filetype = filetype

    def __enter__(self):
        if self.filetype == FileType.BYTE:
            self.file = open(self.file_name, 'wb')
        if self.filetype == FileType.JSON:
            self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def serialize(object, filename, fileType):
    if fileType == FileType.BYTE:
        with SerializeManager(filename, fileType) as f:
            pickle.dump(object, f)
    if fileType == FileType.JSON:
        with SerializeManager(filename, fileType) as f:
            json.dump(object, f)


serialize("Anton", "Anton", FileType.JSON)
user = {"name": "Anton", "id": 123141}
serialize(user, "user.json", FileType.JSON)
