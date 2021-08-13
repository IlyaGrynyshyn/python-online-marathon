import re
from math import sqrt

def figure_perimetr(data):
    x1, y1, x2, y2, x3, y3,x4,y4 = map(int, re.findall(r'\d+', data))
    return sqrt((x1-x2)**2 + (y1-y2)**2) + sqrt((x2-x4)**2 + (y2-y4)**2) + sqrt((x4-x3)**2 + (y4-y3)**2) + sqrt((x3-x1)**2 + (y3-y1)**2)

test1 = test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
