import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(attacker):
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a "+attacker + "is somewhere around "
                "here, and has been terrifying the nearby village....")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty"
                "(but not vert effective) dagger.\n")
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?\n")


def valid_input(weapons, attacker):
    entry = input("(Please enter 1 or 2).")
    if entry == '1':
        house(weapons, attacker)
    elif entry == '2':
        cave(weapons, attacker)
    else:
        valid_input(weapons, attacker)


def house(weapons, attacker):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and steps out a " + attacker)
    print_pause("Eep! This is a " + attacker + "'s house!")
    print_pause("The " + attacker + " attacks you!")
    if 'Sword' not in weapons:
        print_pause("You feel a bit un-prepared for this,"
                    "what with only having a tiny dagger.")
    decide = input("Would you like to fight (1)fight or (2)run away? ")
    if decide == '2':
        field(weapons, attacker)
    elif decide == '1':
        fight(weapons, attacker)
    else:
        play_again()


def cave(weapons, attacker):
    if 'Sword' in weapons:
        print_pause("You peer cautiously into the cave.")
        print_pause("you've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        print_pause("Enter 1 to knock on the door of the house.\n"
                    "Enter 2 to peer into the cave.\n"
                    "What would you like to do?\n")
        valid_input(weapons, attacker)
    else:
        print_pause("You peer cautiously into the cave")
        print_pause("It turns out to be a very small cave")
        print_pause("Your eye catches a glint of metal behind a rock")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly dagger and "
                    "take the sword with you.")
        print_pause("You walk back to the field\n")
        weapons.append('Sword')
        print_pause("Enter 1 to knock on the door of the house.\n"
                    "Enter 2 to peer into the cave.\n")

        valid_input(weapons, attacker)


def fight(weapons, attacker):
    if "Sword" in weapons:
        print_pause("As the "+attacker+" moves to attack,"
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace youself for the attack.")
        print_pause("But the " + attacker +
                    "takes one look at your shiny new toy and run away")
        print_pause("you have rid the town of the " + attacker +
                    ".You are victorious!")
        play_again()
    else:
        print_pause("you do your best..")
        print_pause("But your dagger is not match for the "+attacker+'.')
        print_pause("You have been defeated")
        play_again()


def field(weapons, attacker):
    print_pause("You run back into the field."
                "Luckily, you dont seem to have been followed")
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?\n")
    valid_input(weapons, attacker)


def play_again():
    again = input("Would you like to play again? (y/n)")
    if again == 'y':
        print_pause("Excellent! Restarting the game....\n")
        play_adventure_game()
    elif again == 'n':
        print_pause("Thanks for playing! See you next time")
    else:
        play_again()


def all_in_one():
    inside_house = ['Troll', 'Dragon', 'Pirate', 'gorgon', 'wicked fairie']
    attacker = random.choice(inside_house)
    weapons = ['dagger']
    intro(attacker)
    valid_input(weapons, attacker)


def play_adventure_game():
    all_in_one()


play_adventure_game()
