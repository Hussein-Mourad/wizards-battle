import xml.etree.ElementTree as eT

from Spell import Spell
from Wizard import Wizard


class WizardsBattle:

    def __init__(self):
        self._harry = Wizard("Harry", 100, 500, 3)
        self._voldmort = Wizard("Voldmort", 100, 500, 3)
        self._load_spells()
        self._xml_root = eT.Element("Game")

    def _is_winner(self):
        if self._harry.is_dead() and self._voldmort.is_dead():
            return "\t\tDraw"
        elif self._harry.has_no_energy() and self._voldmort.has_no_energy():
            return "\t\tDraw"
        elif self._harry.is_dead() or self._harry.has_no_energy():
            return "\t\tVoldmort is the winner ..."
        elif self._voldmort.is_dead() or self._voldmort.has_no_energy():
            return "\t\tHarry is the winner ..."
        else:
            return None

    def start_game(self):
        game_round = 1
        game_on = True

        while game_on:
            # keeps asking the user for input until it is correct
            spells = []
            wrong_input = True
            while wrong_input:
                spells = input("Enter the two spells (harry then voldmort):\n").split(" ")
                # if the user enters two strings then it is correct
                if len(spells) == 2:
                    wrong_input = False
                if wrong_input:
                    print("Invalid spell")

            # gets the spell from the user list of spells
            harry_spell = self._harry.find_spell(spells[0])
            voldmort_spell = self._voldmort.find_spell(spells[1])

            # ensures that the user enters his own spell
            if not harry_spell or not voldmort_spell:
                print("Invalid spell")
                continue

            # ensures that the player has enough energy to cast the spell
            if not self._harry.has_enough_energy(harry_spell.get_power()):
                print("Harry doesn't have enough energy")
                continue

            if not self._voldmort.has_enough_energy(voldmort_spell.get_power()):
                print("Voldmort doesn't have enough energy")
                continue

            # Gets the difference between the two spells
            power_difference = abs(harry_spell.get_power() - voldmort_spell.get_power())

            # when the player uses a shield
            if self._harry.has_shields() and (
                    harry_spell.get_name() == "sheild" or harry_spell.get_name() == "shield"):
                # Decreases the number of shields
                self._harry.use_shield()
                # Sets the difference to zero so the health won't be affected
                power_difference = 0

            if self._voldmort.has_shields() and (
                    voldmort_spell.get_name() == "sheild" or voldmort_spell.get_name() == "shield"):
                self._voldmort.use_shield()
                power_difference = 0

            # Decreases the health of the player that used a weaker spell
            if harry_spell.get_power() > voldmort_spell.get_power():
                self._voldmort.decrease_health(power_difference)
            elif voldmort_spell.get_power() > harry_spell.get_power():
                self._harry.decrease_health(power_difference)

            # Decreases the energy of the casted spell
            self._harry.decrease_energy(harry_spell.get_power())
            self._voldmort.decrease_energy(voldmort_spell.get_power())

            # Adds Results to xml tags
            self._log_results(harry_spell, voldmort_spell, game_round)

            # Prints out the results to console
            self._print_result()

            if self._is_winner():
                game_on = False
                # Announce the winner
                print(self._is_winner())
                # Add Result to xml file
                eT.SubElement(self._xml_root, "Game_Result").text = self._is_winner().strip()
                # Write output to xml file
                with open("output.xml", "wb") as f:
                    f.write(eT.tostring(self._xml_root))
            else:
                game_round += 1

    # Reads the spells from the file and adds them to the player spells
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

    def _print_result(self):
        # Ensures that the number always take 3 spaces on the screen
        harry_health = str(max(0, self._harry.get_health())).ljust(3)
        harry_energy = str(max(0, self._harry.get_energy())).ljust(3)
        voldmort_health = str(max(0, self._voldmort.get_health())).ljust(3)
        voldmort_energy = str(max(0, self._voldmort.get_energy())).ljust(3)

        print("\t\tHarry\t\tVoldmort")
        print(
            f"Health : {harry_health}\t\t{voldmort_health}")
        print(
            f"Energy : {harry_energy}\t\t{voldmort_energy}")

    def _log_results(self, harry_spell, voldmort_spell, game_round):
        element1 = eT.SubElement(self._xml_root, "Round_" + str(game_round))

        player1 = eT.SubElement(element1, self._harry.get_name().capitalize())
        spell1 = eT.SubElement(player1, "Casted_Spell")
        spell1.set("name", harry_spell.get_name())
        spell1.set("power", str(harry_spell.get_power()))

        player2 = eT.SubElement(element1, self._voldmort.get_name().capitalize())
        spell2 = eT.SubElement(player2, "Casted_Spell")
        spell2.set("name", voldmort_spell.get_name())
        spell2.set("power", str(voldmort_spell.get_power()))

        eT.SubElement(player1, "Heath").text = str(self._harry.get_health())
        eT.SubElement(player1, "Energy").text = str(self._harry.get_energy())

        eT.SubElement(player2, "Heath").text = str(self._voldmort.get_health())
        eT.SubElement(player2, "Energy").text = str(self._voldmort.get_energy())
