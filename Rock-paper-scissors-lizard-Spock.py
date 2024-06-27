# Rock-paper-scissors-lizard-Spock template
import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


def name_to_number(name):
    pass

    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "name_to_number() find unkonwn name: " + name
        

def number_to_name(number):
    pass
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "number_to_name() find unkown number:",number
        

def rpsls(player_choice): 
    """ 
    player_choice: the name of the player choice
    """
    pass
    
    print ""
    
    # print out the message for the player's choice
    print "Player chooses "+player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses "+comp_choice
    
    diff = (comp_number - player_number) % 5
    
    if (diff == 1) or (diff == 2):
        print "Computer wins!"
    elif (diff == 3) or (diff == 4):
        print "Player wins!"
    else:
        print "Player and computer tie!"
                         
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




