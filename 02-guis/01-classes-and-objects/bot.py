class Bot:
    #set attributes for bot
    def __init__(self, name, age, energy, shield):
        self._name = name
        self._age = age
        self._energy = energy
        self._shield = shield

    #methods to return attributes in correct type
    def get_age(self):
        return int(self._age)

    def get_energy(self):
        return int(self._energy)

    def get_name(self):
        return str(self._name)

    def get_shield(self):
        return int(self._shield)

    #methods to decrease attributes
    def decrement_energy(self, decrement):
        self._energy -= decrement

    def decrement_shield(self, decrement):
        self._shield -= decrement

    #methods to diplay attributes
    def display_age(self):
        print("  /\\")
        print(" /{}\\".format(self._age))
        print("/____\\")

    def display_energy(self):
        print("Energy level:" + ("◊" * int(self._energy)))

    def display_name(self):
        print("-" * (len(self._name) + 2))
        print("|{}|".format(self._name))
        print("-" * (len(self._name) + 2))

    def display_shield(self):
        print("♦♦♦♦♦♦♦")
        print(" ♦♦{}♦♦".format(self._shield))
        print("  ♦♦♦♦")
        print("   ♦♦")

    #method to display summary of all attributes
    def display_summary(self):
        print("-" * (len(self._name) + 9))
        print("|Name: {} |".format(self._name))
        print("|Age: {}".format(self._age) + (" " * len(self._name)) + "|")
        print("|Energy: {}".format(self._energy) + (" " * (len(self._name)-2)) + "|")
        print("|Shield: {}".format(self._shield) + (" " * (len(self._name)-2)) + "|")
        print("-" * (len(self._name) + 10))

    #methods to increase attributes
    def increment_age(self, increment):
        self._age += increment

    def increment_energy(self, increment):
        self._energy += increment

    def increment_sheild(self, increment):
        self._shield += increment

    #method to set the name
    def set_name(self, new_name):
        self._name = new_name

    #sets return string when calling object directly
    def __str__(self):
        return "Name: {}, Age: {}, Energy: {}, Shield: {}".format(self._name, self._age, self._energy, self._shield)


