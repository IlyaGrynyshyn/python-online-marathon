def divide(numerator, denominator):
    try:
        result = numerator / denominator
        return f"Result is {result}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except (ValueError,TypeError):
        return "Value Error! You did not enter a number!"

print(divide('2',0))