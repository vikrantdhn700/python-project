""" This module defines the Warrior class, which is a subclass of GameCharacter. """

from game_character import GameCharacter


class Warrior(GameCharacter):
    def __init__(self, name, health, level, damage):
        super().__init__(name, health, level)
        self.damage = damage

    def sword_attack(self, target):
        target.take_damage(self.damage)
        print(f"{self.name} attacks with {self.damage} damage!")
        print("\n")

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Damage: {self.damage}"
