from sys import exit
from ex35_dead import dead

def show_instructions():
    print "You have entered the Gold Room."
    print "This room is full of gold.  How much do you take?"

def enter_gold_room():    
    show_instructions()
    choice = raw_input("> ")
    try:
        how_much = int(choice)
    except ValueError:
         dead("Man, learn to type a number.")
    else:   
        if how_much < 50:
            print "Nice, you're not greedy, you win!"
            exit(0)
        else:
            dead("You greedy bastard!")