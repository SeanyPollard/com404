# Add your code below for question 6.
# Function to identify species and display result
def identify_species(p_name, p_ability):
    if p_ability == "Fire":
        print(p_name + " is a Fire Pokemon")
    else:
        print(p_name + " is a cool Pokemon")

# Function to identify species, display result and then determine if it can be caught and display result
def can_catch(p_name, p_ability):
    identify_species(p_name, p_ability)
    if p_ability == "Fire":
        print("Can be caught!")
    else:
        print("The Pokemon is too cool to catch!")

# Main run of program
def run():
    # Ask for user to input Pokemon name and ability
    p_name = input("What is the name of the Pokemon?\n")
    p_ability = input("What is their ability?\n")
    # Ask use what they'd like to do
    task = input("Please choose what you'd like to do, 'identify' or 'catch'\n")
    # Run function according to user choice
    if task == "identify":
        identify_species(p_name, p_ability)
    elif task == "catch":
        can_catch(p_name,p_ability)
    else:
        print("Invalid command.")

# Run the program
run()