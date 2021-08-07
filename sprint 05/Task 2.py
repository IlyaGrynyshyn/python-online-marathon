class ToSmallNumberGroupError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return repr(self.text)


def check_number_group(number):
    try:
        if int(number) > 10:
            return f"Number of your group {number} is valid"
        if int(number) < 10:
            raise ToSmallNumberGroupError("We obtain error: Number of your group can't be less than 10")
    except ToSmallNumberGroupError as error:
        return error.text
    except ValueError:
        return "You entered incorrect data. Please try again."



check_number_group(0.8)
check_number_group(-9)
check_number_group("33")