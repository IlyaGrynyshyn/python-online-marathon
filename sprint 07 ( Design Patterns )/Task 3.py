class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def SixWheeler(self):
        return 'SixWheeler'


class Car:
    def __init__(self):
        self.name = "Car"
    def FourWheeler(self):
        return 'FourWheeler'


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""

    def original_dict(self):
        return self.__dict__


