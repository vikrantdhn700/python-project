""" Main module to demonstrate the functionality of the game character system. """

from warrior import Warrior
from wizard import Wizard
from archer import Archer


wizard = Wizard("Dr. Strange", 120, 5, 20)
warrior = Warrior("Thor", 150, 4, 15)
archer = Archer("Hawkeye", 100, 5, 18)


print("\n==================== Character Info ====================")

print(wizard.display_info())
print(warrior.display_info())
print(archer.display_info())


print("\n==================== Battle Start ====================")
wizard.magic_attack(warrior)
warrior.sword_attack(archer)
archer.bow_attack(wizard)

print("\n==================== Post-Battle Character Info ====================")
print(wizard.display_info())
print(warrior.display_info())
print(archer.display_info())
