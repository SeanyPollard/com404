#func to prin ladder based on input
def display_ladder(steps):
    for count in range(steps):
        print("| |\n***")

#func to get steps input
def create_ladder():
    lad_steps = int(input("How many steps remain?\n"))
    display_ladder(lad_steps)

#call func
create_ladder()
