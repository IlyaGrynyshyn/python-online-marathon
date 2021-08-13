import re


def valid_email(email):
    try:
        result = re.search(r'(^[a-z-0-9]+@([a-z]+\.)+[a-z]+$)', email)
        if result:
            return ("Email is valid")
        else:
            raise ValueError("Email is not valid")
    except ValueError as e:
        return ("Email is not valid")


print(valid_email("trafik@ukr.jjjj.com"))
print(valid_email("trafik@ukr.com"))
print(valid_email("trafik@ukr.tel..com"))
print(valid_email("example@source_arth.com"))
