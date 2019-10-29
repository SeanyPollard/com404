# Import module to access functions
import q7

# Initialise variables
min_option = 1
max_option = 4

# Ask user for input
face = input("Please enter an ASCII face for Tutankhamun:\n")
option = int(input("""Please input a number to choose from the following options:
1. Left
2. Right
3. Both
4. Grid\n"""))

# Run function based on option choice and error if invalid selection chosen
if (option < min_option or option > max_option):
    print("Invalid option selection. Please try again.")
elif option == 1:
    q7.left(face)
elif option == 2:
    q7.right(face)
elif option == 3:
    q7.both(face)
elif option == 4:
    q7.grid(face)

