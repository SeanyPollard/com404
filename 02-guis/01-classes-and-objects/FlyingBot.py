#import parent class of superbot
from SuperBot import SuperBot

class FlyingBot(SuperBot):
    #set attributes for flyingbot, inheriting most from superbot
    def __init__(self, name, age, energy, shield, super_power_level, hover):
        super().__init__(name, age, energy, shield, super_power_level)
        self._hover = hover

    #method to return the hover distance
    def get_hover_distance(self):
        return int(self._hover)

    #method to set the hover distance
    def set_hover_distance(self, new_hover):
        self._hover = new_hover

    #sets return string when calling object directly
    def __str__(self):
        return "Name: {}, Age: {}, Energy: {}, Shield: {}, Super Power Level: {}, Hover Distance: {}".format(self._name, self._age, self._energy, self._shield, self._super_power_level, self._hover)