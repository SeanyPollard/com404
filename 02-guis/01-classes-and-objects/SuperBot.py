#import parent class of bot
from bot import Bot

class SuperBot(Bot):
    #set attributes for superbot, inheriting most from bot
    def __init__(self, name, age, energy, shield, super_power_level):
        super().__init__(name, age, energy, shield)
        self._super_power_level = super_power_level

    #method to return the super power level
    def get_super_power_level(self):
        return int(self._super_power_level)

    #method to set the super power level
    def set_super_power_level(self, new_spl):
        self._super_power_level = new_spl

    #sets return string when calling object directly
    def __str__(self):
        return "Name: {}, Age: {}, Energy: {}, Shield: {}, Super Power Level: {}".format(self._name, self._age, self._energy, self._shield, self._super_power_level)
