#store user response to question as integer
zones = int(input('How many zones must I cross?\n'))

#init routine
print("Crossing zones...")

#loop to count down zones until all are crossed
for count in range(zones,0,-1):
    print("...crossed zone " +str(count))

#end routine
print("Crossed all zones. Jumanji!")