# Ask user which cover type
book_cover = input("Is the book hard or soft covered?\n")

# Decide which phrase to output
if book_cover == "soft":

    # ask user more info
    perfect_bound = input("And is it perfect bound?\n")

    # Is it perfect bound?
    if (perfect_bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif book_cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("DUDE! You didn't answer my question!")