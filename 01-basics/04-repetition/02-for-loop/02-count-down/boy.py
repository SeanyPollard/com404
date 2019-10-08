#Ask user for a number
steps = int(input("How far are we from the cave?\n"))

#for loop through steps
for count in range(steps,0,-1):
    print(str(count) + " steps remaining...")

#completion statement
print("We have reached the cave!")