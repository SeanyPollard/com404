# Ask user for 1st number
num_1 = int(input("Gimme a number:\n"))

# Ask user for 2nd number
num_2 = int(input("Gimme another:\n"))

# Initialise operator
print_op = "bigger than"

# Check which is bigger
if num_1 > num_2:
    print_1 = num_1
    print_2 = num_2
elif num_1 < num_2:
    print_1 = num_2
    print_2 = num_1
else:
    print_1 = num_1
    print_2 = num_2
    print_op = "the same as"

# Tell user result
print("So the number " + str(print_1) + " is " + print_op + " " + str(print_2))