from FlyingBot import FlyingBot

def dump_run():
    sean = FlyingBot("Sean",30,5,5,10,100)
    sean.display_name()
    sean.display_age()
    sean.display_energy()
    sean.display_shield()
    sean.display_summary()
    print(sean)

def run():
    sean = FlyingBot("Sean",30,5,5,10,100)
    sean.decrement_energy(2)
    sean.display_energy()

dump_run()