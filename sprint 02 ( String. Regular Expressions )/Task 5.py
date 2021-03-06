import re


def max_population(data):
    a = max([(re.findall(r"(\w*),\d*,\w$", i)[0], int(re.findall(r"(\d*),\w$", i)[0])) for n, i in enumerate(data) if
             n > 0], key=lambda x: int(x[1]))
    return a


data = ["id,name,poppulation,is_capital",
        "3024,eu_kyiv,24834,y",
        "3025,eu_volynia,20231,n",
        "3026,eu_galych,23745,n",
        "4892,me_medina,18038,n",
        "4401,af_cairo,18946,y",
        "4700,me_tabriz,13421,n",
        "4899,me_bagdad,22723,y",
        "6600,af_zulu,09720,n"]

print(max_population(data))
