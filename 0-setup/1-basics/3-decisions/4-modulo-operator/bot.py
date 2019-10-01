# Ask user for a number
num = int(input("What's your favourite number?\n"))

# Work out if odd or even by finding remainder when div by 2
if num % 2 == 0:
    num_type = "even"
else:
    num_type = "odd"

# Inform user about their number
print("Did you know " + str(num) + " is an " + num_type + " number?")