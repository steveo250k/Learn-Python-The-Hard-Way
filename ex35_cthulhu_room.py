from ex35_dead import dead
#from ex35_My_Game import start

def show_instructions():
    print "You have entered the Cthulhu Room."
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    print ""
    print "1. Flee."
    print "2. Eat your head."
    
def enter_cthulhu_room():
    show_instructions()
    
    choice = raw_input("> ")
    
    if choice == "1":
        return
    elif choice == "2":
        dead("Well that was tasty!")
    else:
        enter_cthulhu_room()