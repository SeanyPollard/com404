# com404
COM404 - Problem Solving through Programming

print()
\ breakout character to do something outside the string, need to \\ to display \
\n in string for print creates new line - tidier for input!
""" multiline string
can use end= as keyword in print and change what end is (default /n)
sep= can change seperator when passing multiple arguments (default " ")

= assign
== equal to
> greater than
< less than
!= not equal to
>= greater than or equal to
<>= less than or equal to
+= can be used instead of x = x + a as x += a
-= as above
*= as above
/= as above

if thing is thing:
elif thing is thing:
else:

while this is thing:

for thing in thing:
for thing in range(start,end,step):

def name_of_function:

objects are cooooool maaaaaan
class Thing:
    def __init__(self):             contruct that bad boi
        self.stuff = ""             ooo yeah attribute me up

    def do_stuff(self):
        method code here ohhhhh baby

    def __str__(self):
        return "The string with the stuff {}".format(self.stuff)

now we know what, let's use it (Y)
you = Thing("stuff")                making an object from the class and passing attributes MY GOD
you.do_stuff()                      now I'm calling the object's method from it's class WOW
"I am talking about {} and it's great".format(you.stuff) to call attribute in string

when defining attributes
self.stuff      public to all
self._stuff     protected, not accessed directly but accessible by children classes
self.__stuff    private, not accessed outside the class even through inheritance

Using GUIs
from tkinter import *       AKA bring in all the GUId stuff

Then bring in the class for a blank window
class Gui(Tk):
    def __init__(self):
        super().__init__()

number representations:
int - 123
octal (0-7 only) - 0o123 = 83
hex (0-F) - 0x123 = 291
float - 1.23
exponent - 1.23e4 = 12300
neg exponent - 1.23e-3 = 0.00123
power of - 2**3 = 2*2*2 = 8
integer(floor) division - 6//2 = 3     Normal division always produces float (6/2 = 3.0) so use this is int is needed. Always rounds down to nearest int too so 6.0//4 = 1.0 not 1.5 and -6//4 = -2

float > int - Using a float in a calculation will output a float, even if ints are used too. 