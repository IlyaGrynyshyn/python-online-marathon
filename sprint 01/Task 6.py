def order(a):
    if a == sorted(a):
        return('ascending')
    elif a == sorted(a,reverse = True):
        return ("descending")
    else:
        return ("not sorted")