class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy != None:
            return self.discount_strategy(self)
        else:
            return self.price

    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"



def on_sale_discount(order):
    return order.price * 0.5



def twenty_percent_discount(order):
    return order.price - order.price / 100 * 20

print(Goods(20000))
print(Goods(20000, discount_strategy=twenty_percent_discount))
print(Goods(20000, discount_strategy = on_sale_discount))
print(Goods(20000, discount_strategy = twenty_percent_discount))

