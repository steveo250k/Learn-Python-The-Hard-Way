from ex35_gold_room import enter_gold_room
from ex35_dead import dead

def show_instructions():
    print "You have entered the bear room."
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print ""
    print "1. Take his honey."
    print "2. Taunt the bear."
    print "3. Open door."

def enter_bear_room():
    bear_moved = False
    show_instructions()
        
    while True:
        choice = raw_input("> ")
            
        if choice == "1":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "2" and not bear_moved:
            print "The bear has moved from the door.  You can go through it now." 
            bear_moved = True
        elif choice == "2" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "3" and bear_moved:
            enter_gold_room()
        else:
            if choice == "3" and not bear_moved:
                print "Can't open the door, the bear is blocking it.  Try again."
            else:
                print "I got no idea what that means? Type 1, 2, or 3"