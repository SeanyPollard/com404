#func for underline word
def under(word):
    print(word)
    print("*" * len(word))

#func for overline word
def over(word):
    print("*" * len(word))
    print(word)

#func for over and under line word
def both(word):
    print("*" * len(word))
    print(word)
    print("*" * len(word))

#func for drid
def grid(word,n):
    #create star string
    starline = (("*" * len(word)) + "   ") * n
    starline = starline[:-3]
    #create word string
    wordline = (word + " | ") * n
    wordline = wordline[:-3]
    #loop to print strings
    for count in range(n):
        print(starline)
        print(wordline)
        #print extra start string for the end
        if count == n -1:
            print(starline)


