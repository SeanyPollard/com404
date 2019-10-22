#func for checking change to health
def who(bot,health):
    if bot == "Smiler's Bot":
        health -= 20
        print("Time to jam out of here.")
    elif bot == "Hacker":
        health += 20
        print("Yay! Better follow this one.")
    else:
        print("Phew! Just another emoji.")
    return(health)

#init vars
health = 100

for count in range(0,5,1):
    health = who(input('Oh dear, who is that?\n'),health)

print("Escaped! Health is " + str(health))