class Washing:
    def wath(self):
        return "Washing..."


class Rinsing:
    def rinse(self):
        return 'Rinsing...'


class Spinning:
    def spin(self):
        return 'Spinning...'


class WashingMachine:
    def __init__(self):
        self.wash = Washing().wath()
        self.rinsing = Rinsing().rinse()
        self.spinning = Spinning().spin()
        self.startWashing()

    def startWashing(self):
        print(Washing().wath())
        print(Rinsing().rinse())
        print(Spinning().spin())

washingMachine = WashingMachine()
print(washingMachine)

washingMachine.startWashing()

