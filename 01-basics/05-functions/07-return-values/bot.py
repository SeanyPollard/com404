#func to calc total weight of bots
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

#func to calc average weight of bots
def calc_avg_weight(beep_weight, bop_weight):
    average_weight = sum_weights(beep_weight, bop_weight) / 2
    return average_weight

#func to run programme
def run():
    #gather inputs
    beep_weight = int(input("What is the weight of Beep?\n"))
    bop_weight = int(input("What is the weight of Bop?\n"))
    calc = input("Would you like to calculate sum or average?\n")
    #run calc based on input
    if calc == "sum":
        result = sum_weights(beep_weight, bop_weight)
    else:
        result = calc_avg_weight(beep_weight, bop_weight)
    #output result
    print("The " + calc +" of Beep and Bop's weight is " + str(result))

#run the programme
run()
