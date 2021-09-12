from Spell import Spell
from Wizard import Wizard


class WizardsBattle:

    def __init__(self):
        self._harry = Wizard("Harry", 100, 500, 3)
        self._voldmort = Wizard("Voldmort", 100, 500, 3)
        self._load_spells()

    def _is_winner(self):
        if self._harry.is_dead() and self._voldmort.is_dead():
            return "Draw"
        elif self._harry.has_no_energy() and self._voldmort.has_no_energy():
            return "Draw"
        elif self._harry.is_dead() or self._harry.has_no_energy():
            return "Voldmort is the winner ..."
        elif self._voldmort.is_dead() or self._voldmort.has_no_energy():
            return "Harry is the winner ..."
        else:
            return None

    def start_game(self):
        while True:
            if self._is_winner():
                print(self._is_winner())
                break

            while True:
                spells = input("Enter the two spells (harry then voldmort):\n").split(" ")
                if len(spells) > 1:
                    break
                print("Invalid spell")

            harry_spell = self._harry.find_spell(spells[0])
            voldmort_spell = self._voldmort.find_spell(spells[1])

            if not harry_spell or not voldmort_spell:
                print("Invalid spell")
                continue

            if self._harry.has_enough_energy(harry_spell.get_power()):
                self._harry.decrease_energy(harry_spell.get_power())
                if harry_spell.get_name() != voldmort_spell.get_name():
                    if harry_spell.get_name() == "sheild" or harry_spell.get_name() == "shield":
                        self._harry.use_shield()
                    self._voldmort.decrease_health(harry_spell.get_power())
            else:
                print("Harry doesn't have enough energy")

            if self._voldmort.has_enough_energy(voldmort_spell.get_power()):
                self._voldmort.decrease_energy(voldmort_spell.get_power())
                if harry_spell.get_name() != voldmort_spell.get_name():
                    self._harry.decrease_health(voldmort_spell.get_power())
            else:
                print("Voldmort doesn't have enough energy")

            harry_health = str(max(0, self._harry.get_health())).ljust(3)
            harry_energy = str(max(0, self._harry.get_energy())).ljust(3)
            voldmort_health = str(max(0, self._voldmort.get_health())).ljust(3)
            voldmort_energy = str(max(0, self._voldmort.get_energy())).ljust(3)

            print("\t\tHarry\t\tVoldmort")
            print(
                f"Health : {harry_health}\t\t{voldmort_health}")
            print(
                f"Energy : {harry_energy}\t\t{voldmort_energy}")

    def _load_spells(self):
        with open("spells.txt", "r") as f:
            for line in f:
                buffer = line.split(" ")
                spell_type = buffer[0]
                spell_name = buffer[1]
                spell_power = int(buffer[2])

                if spell_type == "A":
                    self._harry.add_spell(Spell(spell_name, spell_power))
                    self._voldmort.add_spell(Spell(spell_name, spell_power))
                elif spell_type == "H":
                    self._harry.add_spell(Spell(spell_name, spell_power))
                else:
                    self._voldmort.add_spell(Spell(spell_name, spell_power))
