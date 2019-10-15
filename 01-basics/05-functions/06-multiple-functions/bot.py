def display_ladder(steps):
    for count in range(steps):
        print("| |\n***")

def create_ladder():
    lad_steps = int(input("How many steps remain?\n"))
    display_ladder(lad_steps)

create_ladder()
