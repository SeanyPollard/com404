# Add your code below for question 4.
def trap(who, where):
    # Write your code here (remember to indent correctly)
    if (who == "Jerry" and where == "Inside"):
        print("I will have mouse stew tonight!")
    elif (who == "Spike" and where == "Inside"):
        print("Oh dear! I better hide!")
    else:
        print("I will get Jerry soon!")

# The following are calls to the function for testing purposes
trap("Spike", "Inside")
trap("Jerry", "Outside")
trap("Jerry", "Inside")