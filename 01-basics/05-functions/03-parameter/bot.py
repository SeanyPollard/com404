#escape_by func to determine response
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder i moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot scape that way! The boulder is in the way!")

#call escape_by with input 1
escape_by("jumping over")
#call escape_by with input 2
escape_by("running around")
#call escape_by with input 3
escape_by("going deeper")