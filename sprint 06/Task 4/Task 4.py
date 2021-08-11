import json


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as file:
            data = json.load(file)
            return cls(data["full_name"], data["avg_rank"], data["courses"])

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students
        if type(self.students) is dict:
            self.students = [students]

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, "a") as file:
            list_to_dump = []
            for each in list_of_groups:
                group_info = each.__dict__
                print(group_info)
                list_to_dump.append({'title': group_info["title"], 'students': group_info["students"]})
            json.dump(list_to_dump, file)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as group_file:
            data = json.load(group_file)
            return cls(group_file.name[:-5], data)

    def __str__(self):
        list_of_stud = []
        if type(self.students) is list:
            for each in self.students:
                fullname = each["full_name"]
                avgrank = each["avg_rank"]
                courses = each["courses"]
                list_of_stud.append(f"{fullname} ({avgrank}): {courses}")
        else:
            fullname = self.students["full_name"]
            avgrank = self.students["avg_rank"]
            courses = self.students["courses"]
            list_of_stud.append(f"{fullname} ({avgrank}): {courses}")
        return f"{self.title}: {list_of_stud}"


g1 = Group.create_group_from_file("2020-01.json")
g2 = Group.create_group_from_file("2020_2 (2).json")
Group.serialize_to_json([g1, g2], "g1")
