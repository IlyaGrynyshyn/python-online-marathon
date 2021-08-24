def create(name):
    return lambda x: True if x == name else False


tom = create("pass_for_Tom")
print(tom("pass_for_Tom"))
