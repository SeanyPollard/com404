class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("-" * (len(self.name) + 2))
        print("|{}|".format(self.name))
        print("-" * (len(self.name) + 2))

    def display_age(self):
        print("  /\\")
        print(" /{}\\".format(self.age))
        print("/____\\")

    def display_energy(self):
        print("Energy level:" + ("◊" * int(self.energy)))

    def display_shield(self):
        print("♦♦♦♦♦♦♦")
        print(" ♦♦{}♦♦".format(self.shield))
        print("  ♦♦♦♦")
        print("   ♦♦")

    def display_summary(self):
        print("-" * (len(self.name) + 9))
        print("|Name: {} |".format(self.name))
        print("|Age: {}".format(self.age) + (" " * len(self.name)) + "|")
        print("|Energy: {}".format(self.energy) + (" " * (len(self.name)-2)) + "|")
        print("|Shield: {}".format(self.shield) + (" " * (len(self.name)-2)) + "|")
        print("-" * (len(self.name) + 10))

    def __str__(self):
        return "Name: {}, Age: {}, Energy: {}, Shield: {}".format(self.name, self.age, self.energy, self. shield)

sean = Bot("Sean","30","5","5")
sean.display_name()
sean.display_age()
sean.display_energy()
sean.display_shield()
sean.display_summary()
print(sean)
