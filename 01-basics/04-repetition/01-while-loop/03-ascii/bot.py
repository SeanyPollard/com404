#Ask user for number of bars to charge
bars = int(input("How many bars should be charged?\n"))

#Initialise counter and ASCII
counter = 0
charge = "$"

#While less than input bars, keep charging
while counter < bars:
    counter += 1
    print("Charging: " + (charge * counter))

#Completion statement
print("The battery is fully charged")
