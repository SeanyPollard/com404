# Ask user for painting direction
dir_input = input("Yo! Which way should I paint?\n")

# Decide which way to paint from input
if dir_input == "Up":
    dir_output = "upwards"
elif dir_input == "Down":
    dir_output = "downwards"
elif dir_input == "Left":
    dir_output = "leftwards"
elif dir_input == "Right":
    dir_output = "rightwards"
else:
    dir_output = "wait, that isn't a direction"

# output result to user
print("The direction in which I shall paint is... " + dir_output + "!")