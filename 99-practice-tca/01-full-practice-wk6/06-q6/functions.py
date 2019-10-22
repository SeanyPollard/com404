#init funcs
def is_league_united(hero1,hero2):
    if (hero1 == "Superman" and hero2 == "Wonder Woman") or (hero1 == "Wonder Woman" and hero2 == "Superman"):
        return("True")
    else:
        return("False")

def decide_plan(hero1,hero2):
    if is_league_united(hero1,hero2) == "True":
        print("Time to save the world!")
    else:
        print("We must unite the league!")

def run():
    hero1 = input('What is the name of the first hero?\n')
    hero2 = input('What is the name of the second hero?\n')
    decide = input("""Please input one of the following:
    league - to see if the league is united
    plan - to decide the plan\n""")

    if decide == "league":
        print(is_league_united(hero1,hero2))
    elif decide == "plan":
        decide_plan(hero1,hero2)
    else:
        print("Invalid command. Please try again")

#run the program
run()
