#Ask user for a number
brightness = int(input("What level of brightness is required?\n"))

#init vars and statement
light = "**"
total = ""
print("Adjusting brightness...")

#for loop to increment
for count in range(0,brightness,2):
    total += light
    print("Beep's brightness level: " +  total)
    print("Bop's brightness level: " +  total + "\n")

#completion statement
print("Adjustments complete!")