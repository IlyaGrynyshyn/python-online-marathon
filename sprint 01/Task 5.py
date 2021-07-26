def toPostFixExpression(e):
    num = "".join(n for n in e if n.isdecimal())
    sym = "".join(n for n in e if not n.isdecimal())
    a = list(num + sym)
    return a