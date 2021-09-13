from Spell import Spell


class Wizard:

    def __init__(self, name, heath, energy, shield):
        self._name = name
        self._health = heath
        self._energy = energy
        self._shield = shield
        self._spells = []

    def get_name(self) -> str:
        return self._name

    def get_health(self) -> int:
        return self._health

    def decrease_health(self, amount: int):
        self._health -= amount

    def get_energy(self) -> int:
        return self._energy

    def decrease_energy(self, amount: int):
        self._energy -= amount

    def get_shield(self):
        return self._shield

    def has_shields(self) -> bool:
        return self._shield > 0

    def use_shield(self):
        if self._shield > 0:
            self._shield -= 1

    def get_spells(self):
        return self._spells

    def find_spell(self, name: str) -> Spell:
        for spell in self._spells:
            if spell.get_name().lower() == name.lower():
                return spell

    def add_spell(self, spell: Spell):
        self._spells.append(spell)

    def is_dead(self) -> bool:
        return self._health <= 0

    def has_no_energy(self) -> bool:
        return self._energy <= 0

    def has_enough_energy(self, spell_power: int) -> bool:
        return self._energy >= spell_power
