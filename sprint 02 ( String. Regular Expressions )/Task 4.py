import re


def pretty_message(data):
    b = (re.sub(r'([a-z]+?)\1+', r'\1', data))
    return b


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))
