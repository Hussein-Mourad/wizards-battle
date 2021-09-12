class Spell:
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_power(self):
        return self._power

    def set_power(self, power):
        self._power = power

    def __str__(self):
        return self._name + " " + str(self._power)
