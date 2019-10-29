# Add your code below for question 7.
# Left function
def left(face):
    print(("/\\" *len(face)) + " " + face)

# Right function
def right(face):
    print(face + " " + ("/\\" * len(face)))

# Both function
def both(face):
    print(("/\\" *len(face)) + " " + face + " " + ("/\\" * len(face)))

# Grid function
def grid(face):
    # Ask user for grid size
    size = int(input("What is the size of the grid?\n"))
    # Iterate to print grid based on user input
    for count in range(0,size,1):
        print((("/\\" *len(face)) + " " + face + " " + ("/\\" * len(face))) * size)

