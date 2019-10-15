#func to dispay input in a ascii box
def box_it(word):
    print(" "+("-"*len(word))+" ")
    print("|"+word+"|")
    print(" "+("-"*len(word))+" ")

#func to display input in lower-case
def lower_it(word):
    print(str.lower(word))

#func to display input in upper-case
def upper_it(word):
    print(str.upper(word))

#func to display input mirrored
def mirror_it(word):
    phrase = word + " | "
    for count in range(len(word),0,-1):
        phrase += word[count-1]
    print(phrase)

#func to repeat input user input times and alt between upper and lower case
def repeat_it(word):
    switch = True
    repeat = int(input("How many times should I repeat the word?\n"))
    for count in range(repeat):
        if switch:
            switch = False
            print(str.upper(word))
        else:
            switch = True
            print(str.lower(word))

#func to run programme
def run():
    word = input("Please enter a word:\n")
    thing = int(input("""Please pick an option:
    1. Display in Box
    2. Display in lower-case
    3. Display in upper-case
    4. Display mirrored
    5. Repeat\n"""))
    if thing == 1:
        box_it(word)
    elif thing == 2:
        lower_it(word)
    elif thing == 3:
        upper_it(word)
    elif thing == 4:
        mirror_it(word)
    else:
        repeat_it(word)

#run programme
run()