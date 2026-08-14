""" A class representing a game character """


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} has {damage} damage and now has {self.health} health.")

    def display_info(self):
        return f"Name: {self.name}, Health: {self.health}, Level: {self.level}"
