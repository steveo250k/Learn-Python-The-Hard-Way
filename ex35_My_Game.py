from sys import exit
from ex35_bear_room import enter_bear_room
from ex35_dead import dead
from ex35_cthulhu_room import enter_cthulhu_room

def show_instructions():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which door do you take?"
    print ""
    print "1. left"
    print "2. right"

    
def start():
    show_instructions()
    
    while True:
        choice = raw_input("> ")
    
        if choice == "1":
            enter_bear_room()
        elif choice == "2":
            enter_cthulhu_room()
        else:
            dead("Type a 1 or a 2 dummy.  Start over.")
        
        show_instructions()

start()
            