#import funcs from functions.py
from functions import under, over, both, grid

#main routine run
def run():
    #word input from user
    word = input('Please enter a word:\n')
    #option in put from user
    option = int(input("""Please choose from the following options:
    1 - underline the word
    2 - overline the word
    3 - under and overline the word
    4 - display the word in a grid\n"""))

    #decision based on option input
    if option == 1:
        under(word)
    elif option == 2:
        over(word)
    elif option == 3:
        both(word)
    elif option == 4:
        n = int(input('Please input a grid size:\n'))
        grid(word,n)

#run the program
run()