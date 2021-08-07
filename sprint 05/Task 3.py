class MyError(Exception):
    def __init__(self,text):
        self.text = text

    def __str__(self):
        return repr(self.text)


def check_positive(number):
    try:
        if float(number) > 0:
            return f'You input positive number: {float(number)}'
        if float(number) < 0:
            raise MyError(f"You input negative number: {float(number)} Try again.")
    except MyError as error:
        return error.text
    except ValueError:
        return "Error type: ValueError!"
# enter your code

print(check_positive (24) )
print(check_positive (-21.0) )
print(check_positive ('cd') )