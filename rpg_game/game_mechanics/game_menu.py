# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and
# programming. Eager to learn Python, I thought it would
# be an awesome idea to develop a game, taking Star Wars
# as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for the game's start and player menu]
"""

import time

from game_mechanics import game_terminal as term


def game_intro():
    """
    [Start of the game's intro function]
    """
    term.clear()
    time.sleep(1)
    term.bprint("In the future,\nin a star system very far away...\n")
    time.sleep(1)
    term.yprint("Black Star")
    term.wprint("A Text-Based Adventure")
    term.wprint("Developed by Ryan Butler")
    time.sleep(2)
    term.clear()


def game_menu():
    """
    [Menu function, to start game or quit game.]
    """
    term.clear()
    term.yprint("Black Star")
    term.wprint("A Text-Based Adventure\n\n")
    term.wprint("MAIN MENU\n1. Play\n2. Quit")
    # Playing the game
    while True:
        player_input = term.player_input()

        # Start game menu option
        if player_input == "1":
            term.bprint("Get ready, starting game...")
            time.sleep(2)
            term.clear()
            return player_input

        # Quit game menu option
        elif player_input == "2":
            term.bprint("Goodbye, see you again soon...")
            time.sleep(2)
            term.clear()
            break

        else:
            term.rprint("Please enter correct menu option...")
            time.sleep(3)
            term.clear()
            term.yprint("Black Star")
            term.wprint("A Text-Based Adventure\n\n")
            term.wprint("MAIN MENU\n1. Play\n2. Quit")
            continue

    return player_input
