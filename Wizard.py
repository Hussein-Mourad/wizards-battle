class Wizard:

    def __init__(self, name, heath, energy, shield):
        self._name = name
        self._health = heath
        self._energy = energy
        self._shield = shield
        self._spells = []

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def decrease_health(self, amount):
        self._health -= amount

    def get_energy(self):
        return self._energy

    def decrease_energy(self, amount):
        self._energy -= amount

    def get_shield(self):
        return self._shield

    def use_shield(self):
        if self._shield > 0:
            self._shield -= 1

    def get_spells(self):
        return self._spells

    def find_spell(self, name: str):
        for spell in self._spells:
            if spell.get_name().lower() == name.lower():
                return spell
        return None

    def add_spell(self, spell):
        self._spells.append(spell)

    def is_dead(self):
        return self._health <= 0

    def has_no_energy(self):
        return self._energy <= 0

    def has_enough_energy(self, spell_power):
        return self._energy >= spell_power
