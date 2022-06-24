import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right there is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) dagger.\n")


def fight(enemy, inventory):
    # Things that happen when the player fights
    if "sword" not in inventory:
        print_pause(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger.")
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
        play_again = input(
            "Would you like to play again? (y/n)\n").lower()
        if play_again == "y":
            print_pause("Excellent! Restarting the game ...\n")
            play_game()

        else:
            print_pause("Thanks for playing! See you next time.")

    elif "sword" in inventory:
        print_pause(
            f"As the {enemy} moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(
            f"But the {enemy} takes one look at your shiny "
            "new toy and runs away!")
        print_pause(
            f"You have rid the town of the {enemy}. You are victorious!")


def cave(enemy, inventory):
    # Things that happen to the player goes in the cave
    if "sword" in inventory:
        print_pause("You peer cautiously into the cave.")
        print_pause(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        house(enemy, inventory)

    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(
            "You discard your silly old dagger and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        inventory.append("sword")
        house(enemy, inventory)


def field(enemy, inventory):
    # Things that happen when the player runs back to the field
    print_pause(
        "You run back into the field. "
        "Luckily, you don't seem to have been followed.")
    house(enemy, inventory)


def house(enemy, inventory):
    # Things that happen to the player in the house
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2.)\n")

    if choice == "1":
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door opens "
                    f"and out steps a {enemy}.")
        print_pause(f"Eep! This is the {enemy}'s house!")
        print_pause(f"The {enemy} attacks you!")
        choice1 = input("Would you like to (1) fight or (2) run away?\n"
                        "Please enter 1 or 2.\n")

        if choice1 == "1":
            fight(enemy, inventory)

        else:
            field(enemy, inventory)

    elif choice == "2":
        cave(enemy, inventory)

    else:
        choice = input("(Please enter 1 or 2.)\n")


def play_game():
    enemy_choice = ["witch", "troll", "bear", "wicked fairie"]
    enemy = random.choice(enemy_choice)
    inventory = []  # to add sword
    intro(enemy)
    house(enemy, inventory)


play_game()
