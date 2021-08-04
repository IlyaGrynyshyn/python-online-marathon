class Pizza():
    order_num = 0

    def __init__(self, ingredients):
        Pizza.order_num += 1
        self.order_number = Pizza.order_num
        self.ingredients = ingredients

    @classmethod
    def garden_feast(cls):
        ingredients = ["spinach", "olives", "mushroom"]
        return cls(ingredients)

    @classmethod
    def hawaiian(cls):
        ingredients = ["ham", "pineapple"]
        return cls(ingredients)

    @classmethod
    def meat_festival(cls):
        ingredients = ["beef", "meatball", "bacon"]
        return cls(ingredients)


p2 = Pizza.meat_festival()
print(p2.ingredients)

print(p2.order_number)

p1 = Pizza(['bacon', 'parmesan', 'ham'])
print(p1.ingredients)
